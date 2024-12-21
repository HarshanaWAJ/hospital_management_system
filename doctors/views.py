from django.shortcuts import render, redirect
from .reg_doctor_form import DoctorForm

# Create your views here.
def register_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data (creates a new Doctor instance)
            return redirect('doctor_list')  # Redirect after successful form submission
        else:
            # Print form errors if form is not valid
            print("Form is not valid!")
            print(form.errors)  # This will print the error dictionary to the console
    else:
        form = DoctorForm()  # Create an empty form instance

    return render(request, 'doctor.registration.html', {'form': form})
