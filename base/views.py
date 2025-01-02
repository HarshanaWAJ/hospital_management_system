from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .contact_form import MessageForm
from django.http import JsonResponse

from .utils.analyze_message_util import analyze_sentiment, is_question, calculate_service_quality

# Register
from django.shortcuts import render, redirect
from django.contrib import messages
from .register_form import UserRegisterForm

# Send Mail
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from appoinments.models import Appointment
# Views

#Home with Contact Form
def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # Set success message in session to display after redirect
            request.session['message'] = 'success'
            return redirect('home')
        else:
            # Set error message in session to display after redirect
            request.session['message'] = 'error'
            return redirect('home')
    else:
        form = MessageForm()

    # Check if there is a message in the session and clear it
    message = request.session.get('message', None)
    if message:
        del request.session['message']

    return render(request, 'home.html', {'contact_form': form, 'message': message})


# Delete Message View
def delete_message(request, message_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Try to get the message by ID and delete it
        message = get_object_or_404(Message, id=message_id)     
        try:
            message.delete()
            return JsonResponse({'message': 'Success'}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Error', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)


# Login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Get User Details
            user_details = {
                'is_super_user': user.is_superuser,
                'is_user': user.is_user,
                'is_admin': user.is_admin,
                'is_staff': user.is_staff,
                'is_doctor': user.is_doctor
            }
            print(user_details)
            login(request, user)

            # Check user roles and redirect accordingly
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirect superuser to the admin dashboard
            elif user.is_user:
                return redirect('user_dashboard')
            elif user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_staff:
                return redirect('staff_dashboard')
            elif user.is_doctor:
                return redirect('doctor_dashboard')
            else:
                messages.error(request, "No Authorities")
        else:
            # Instead of messages, pass an error flag to the context
            return render(request, 'login.html', {'invalid_credentials': True})

    return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # Check form validity
            user = form.save()  # Save the user with the custom fields
            # Send account creation success email
            send_account_creation_email(user)

            messages.success(request, 'Your account has been created!')
            return redirect('login')  # Redirect after successful registration
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'register_form': form})


# Admin Messages    
def admin_message(request):
    # Fetch all messages
    admin_messages = Message.objects.all()

    # Initialize counters for overall service quality
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    # Analyze sentiment and question for each message
    analyzed_messages = []
    for message in admin_messages:
        sentiment = analyze_sentiment(message.message)  # Sentiment analysis
        is_question_detected = is_question(message.message)  # Check if it's a question
        service_quality = calculate_service_quality(sentiment)  # Calculate service quality

        # Increment counters for overall service quality
        if sentiment == 'positive':
            positive_count += 1
        elif sentiment == 'negative':
            negative_count += 1
        else:
            neutral_count += 1

        analyzed_messages.append({
            'message': message,
            'sentiment': sentiment,
            'is_question': is_question_detected,
            'service_quality': service_quality,
        })

    # Determine overall service quality and percentages
    total_count = len(admin_messages)

    # Calculate the percentage for each sentiment category
    if total_count > 0:
        positive_percentage = (positive_count / total_count) * 100
        negative_percentage = (negative_count / total_count) * 100
        neutral_percentage = (neutral_count / total_count) * 100
        
        # Calculate the total service quality percentage (positive minus negative)
        total_percentage = positive_percentage - negative_percentage
    else:
        positive_percentage = negative_percentage = neutral_percentage = total_percentage = 0

    # Determine overall service quality
    if positive_count > negative_count:
        overall_service_quality = 'Excellent'
        quality_color = 'green'
    elif negative_count > positive_count:
        overall_service_quality = 'Poor'
        quality_color = 'red'
    else:
        overall_service_quality = 'Neutral'
        quality_color = 'yellow'

    # Context with the analyzed messages, overall service quality, and percentages
    context = {
        'admin_messages': analyzed_messages,
        'overall_service_quality': overall_service_quality,
        'quality_color': quality_color,
        'positive_percentage': positive_percentage,
        'negative_percentage': negative_percentage,
        'neutral_percentage': neutral_percentage,
        'total_service_quality_percentage': total_percentage,  # Total percentage to show
    }

    return render(request, 'admin.message.html', context)
# Dashboards
# UserDashboard View
@login_required
def user_dashboard(request):
    total_appointment_count = Appointment.objects.filter(user=request.user.id).count()  # Get the total appointment count
    total_confirmed_appointment_count = Appointment.objects.filter(status='Confirmed', user=request.user.id).count()
    total_pending_appointment_count = Appointment.objects.filter(status='Pending', user=request.user.id).count()
    total_cancelled_appointment_count = Appointment.objects.filter(status='Cancelled', user=request.user.id).count()

    return render(request, 'user_dashboard.html', {
        'total_appointment_count': total_appointment_count,
        'total_confirmed_appointment_count': total_confirmed_appointment_count,
        'total_pending_appointment_count': total_pending_appointment_count,
        'total_cancelled_appointment_count': total_cancelled_appointment_count
    }) 

# AdminDashboard View
@login_required
def admin_dashboard(request):
    total_appointment_count = Appointment.objects.count()  # Get the total appointment count
    total_confirmed_appointment_count = Appointment.objects.filter(status='Confirmed').count()
    total_pending_appointment_count = Appointment.objects.filter(status='Pending').count()
    total_cancelled_appointment_count = Appointment.objects.filter(status='Cancelled').count()
    return render(request, 'admin.dashboard.html', {
        'total_appointment_count': total_appointment_count,
        'total_confirmed_appointment_count': total_confirmed_appointment_count,
        'total_pending_appointment_count': total_pending_appointment_count,
        'total_cancelled_appointment_count': total_cancelled_appointment_count
    }) 

# DoctorDashboard View
from appoinments.models import Appointment
@login_required
def doctor_dashboard(request):
    total_appointment_count = Appointment.objects.filter(referring_doctor = request.user).count()  # Get the total appointment count
    total_confirmed_appointment_count = Appointment.objects.filter(status='Confirmed', referring_doctor = request.user).count()
    total_pending_appointment_count = Appointment.objects.filter(status='Pending', referring_doctor = request.user).count()
    total_cancelled_appointment_count = Appointment.objects.filter(status='Cancelled', referring_doctor = request.user).count()
    return render(request, 'doctor.dashboard.html', {
        'total_appointment_count': total_appointment_count,
        'total_confirmed_appointment_count': total_confirmed_appointment_count,
        'total_pending_appointment_count': total_pending_appointment_count,
        'total_cancelled_appointment_count': total_cancelled_appointment_count
    }) 

# StaffDashboard View
@login_required
def staff_dashboard(request):
    return render(request, 'staff.dashboard.html') 


import os
from django.shortcuts import render

def show_user_activity(request):
    log_file_path = 'user_activity.log'
    # Check if the log file exists
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.readlines()  # Read the log file line by line
    else:
        log_content = []

    # Pass the log entries to the template
    return render(request, 'user_activity.html', {'log_entries': log_content})

# --------------------------------------------------------------------------------------------------------------
# Account Registration Mail Sending
def send_account_creation_email(user):
    # Logging user information for debugging (you might remove this in production)
    print(user)
    
    # Define subject and message
    subject = 'Welcome to Carebridge - Account Successfully Created'
    
    message = f"""
    Dear {user.username},
    
    We are pleased to inform you that your account has been successfully created on the Carebridge platform. 
    
    You can now log in using your credentials and start exploring the features we offer. If you encounter any issues or have questions, our support team is available to assist you.

    Thank you for choosing Carebridge. We look forward to serving you and hope you have a great experience.

    Best regards,
    The Carebridge Team
    Support: support@carebridge.com
    Website: www.carebridge.com
    """
    
    # Send the email using Django's send_mail function
    send_mail(
        subject,
        message,
        'developmentmail2024@gmail.com',  # Sender's email address
        [user.email],  # Recipient's email address
        fail_silently=False,
    )

    
# ------------------------------------------------------------------------------------------------------------------------------------
