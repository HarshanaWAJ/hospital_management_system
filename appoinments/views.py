from django.shortcuts import render, redirect
from .AppointmentForm import AppointmentForm
from django.contrib import messages  # Import Django's message framework

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new appointment record to the database
            messages.success(request, 'Your appointment has been successfully booked!')  # Success message
            return redirect('home')  # Redirect after successful submission
        else:
            messages.error(request, 'There was an error with your form submission. Please try again.')  # Error message
    else:
        form = AppointmentForm()  # Create an empty form for GET requests

    return render(request, 'make.appoinments.html', {'appointments_form': form})
