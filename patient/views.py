from django.shortcuts import render, redirect
from .opd_patient_reg_form import PatientForm

# Create your views here.
def register_opd_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the data into the database
            return redirect('patient_list')  # Redirect to a list page or another view after saving
    else:
        form = PatientForm()

    return render(request, 'add.opd.patient.html', {'form': form})