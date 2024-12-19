from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .contact_form import MessageForm
from django.urls import reverse
from django.http import JsonResponse

from .utils.analyze_message_util import analyze_sentiment, is_question, calculate_service_quality
from django.views.decorators.csrf import csrf_exempt



# Create views here.

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
def login(request):
    return render(request, 'login.html')

# Register
from django.shortcuts import render, redirect
from django.contrib import messages
from .register_form import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
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

