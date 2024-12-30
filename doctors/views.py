from django.shortcuts import render, redirect
from .reg_doctor_form import DoctorForm
from .models import Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data (creates a new Doctor instance)
            return redirect('doctor_management')  # Redirect after successful form submission
        else:
            # Print form errors if form is not valid
            print("Form is not valid!")
            print(form.errors)  # This will print the error dictionary to the console
    else:
        form = DoctorForm()  # Create an empty form instance

    return render(request, 'doctor.registration.html', {'form': form})


@login_required
def doctor_management(request):
    doctor_list = Doctor.objects.all()
    return render(request, 'doctor.management.html', {
        'doctor_list': doctor_list
    })

@login_required
def delete_doctor(request, id):
    admin = Doctor.objects.get(id=id)
    admin.delete()
    return redirect('doctor_management')