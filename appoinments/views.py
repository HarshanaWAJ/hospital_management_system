from django.shortcuts import render, redirect, get_object_or_404

from appoinments.models import Appointment
from .AppointmentForm import AppointmentForm
from django.contrib import messages  # Import Django's message framework
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if not form.instance.status:
            form.instance.status = 'Pending'
        # Check if the form is valid
        if form.is_valid():
            form.save()  # Pass the logged-in user during save
            messages.success(request, 'Your appointment has been successfully booked!')
            return redirect('my_appointments')
        else:
            print("Form is invalid. Errors: ")
            print(form.errors)  # Print all form errors
            
            # Optionally, print specific field errors
            for field in form:
                if field.errors:
                    print(f"Errors for {field.name}: {field.errors}")
            
            messages.error(request, 'There was an error with your form submission. Please try again.')
    else:
        form = AppointmentForm(initial={'user': request.user})  # Pass the user to the form in GET request

    return render(request, 'make.appointments.html', {'appointments_form': form})

def user_view_appointments(request):
    total_appointments_count = Appointment.objects.filter(user=request.user.id).count()
    pending_appointments_count = Appointment.objects.filter(user=request.user.id, status='Pending').count()
    accepted_appointments_count = Appointment.objects.filter(user=request.user.id, status='Confirmed').count()
    cancelled_appointments_count = Appointment.objects.filter(user=request.user.id, status='Cancelled').count()

    pending_appointments = Appointment.objects.filter(user=request.user.id, status='Pending')
    accepted_appointments = Appointment.objects.filter(user=request.user.id, status='Confirmed')
    cancelled_appointments = Appointment.objects.filter(user=request.user.id, status='Cancelled')
    return render(request, 'user.appointments.html', {
        'pending_appointments': pending_appointments,
        'accepted_appointments': accepted_appointments,
        'cancelled_appointments': cancelled_appointments,
        'total_appointments_count': total_appointments_count,
        'pending_appointments_count': pending_appointments_count,
        'accepted_appointments_count': accepted_appointments_count,
        'cancelled_appointments_count': cancelled_appointments_count
    })

def delete_appointment(request, id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=id)
        current_time = timezone.now()
        time_diff = appointment.appointment_date - current_time

        print(time_diff)
        
        if time_diff > timedelta(hours=1) or time_diff < timedelta(0) :  # If the appointment is more than 1 hour away
            appointment.delete()  # Delete the appointment
            messages.success(request, 'Your appointment has been successfully deleted.')
            return redirect('my_appointments')  # Redirect to 'my_appointments' after successful deletion
        else:
            messages.error(request, 'The appointment time is too close. Cancellation is not allowed at this time.')
            return redirect('my_appointments')  # Redirect back to 'my_appointments' with an error message

    return redirect('my_appointments')  # Default redirect if not a POST request


def doctor_view_pending_appointments(request):
    # Query for pending, accepted, and cancelled appointments
    pending_appointments = Appointment.objects.filter(referring_doctor=request.user, status='Pending')
    accepted_appointments = Appointment.objects.filter(referring_doctor=request.user.id, status='Confirmed')
    cancelled_appointments = Appointment.objects.filter(referring_doctor=request.user.id, status='Cancelled')
    
    # Render the template and pass the context variables
    return render(request, 'doctor.appointments.html', {
        'pending_appointments': pending_appointments,
        'accepted_appointments': accepted_appointments,
        'cancelled_appointments': cancelled_appointments
    })


@csrf_exempt
def accept_reject_appointment(request, id, action):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=id)

        if action == 'accept':
            appointment.status = 'Confirmed'
        elif action == 'reject':
            appointment.status = 'Cancelled'

        appointment.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)