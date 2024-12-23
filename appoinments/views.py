from django.shortcuts import render, redirect

from appoinments.models import Appointment
from .AppointmentForm import AppointmentForm
from django.contrib import messages  # Import Django's message framework


def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            form.save()  # Pass the logged-in user during save
            messages.success(request, 'Your appointment has been successfully booked!')
            return redirect('appointment_success')
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
    appointments = Appointment.objects.filter(user=request.user.id)
    print(appointments)
    return render(request, 'user.appointments.html', {'appointments': appointments})

def doctor_view_appointments(request):
    appointments = Appointment.objects.filter(referring_doctor=request.user)
    print(appointments)
    return render(request, 'doctor.appointments.html', {'appointments': appointments})