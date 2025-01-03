from django.shortcuts import render, redirect
from .opd_patient_reg_form import PatientForm
from .admitted_patient_reg_form import AdmittedPatientForm  # Import the PatientForm

def register_opd_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data into the database
            return redirect('staff_dashboard')  # Redirect to a list page or another view after saving
        else:
            # If form is not valid, we render the form again with errors
            return render(request, 'add.opd.patient.html', {'form': form})
    else:
        form = PatientForm()

    return render(request, 'add.opd.patient.html', {'form': form})

def register_admitted_patient(request):
    if request.method == 'POST':
        form = AdmittedPatientForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data into the database
            return redirect('staff_dashboard')  # Redirect to a list page or another view after saving
        else:
            # If form is not valid, we render the form again with errors
            return render(request, 'add.admitted.patient.html', {'form': form})
    else:
        form = AdmittedPatientForm()

    return render(request, 'add.admitted.patient.html', {'form': form})