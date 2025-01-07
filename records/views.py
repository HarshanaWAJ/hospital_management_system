from django.shortcuts import render, redirect
from .add_record_form import MedicalRecordForm
from .models import Record

def add_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)  # Bind the form with POST data
        if form.is_valid():  # Validate the form
            form.save()  # Save the record to the database
            return redirect('doctor_dashboard')  # Redirect to a success page
        else:
            print(form.errors)  # Print the form errors for debugging
    else:
        form = MedicalRecordForm()  # Initialize an empty form if GET request

    return render(request, 'add.record.html', {'form': form})


def view_record(request):
    record_list = Record.objects.all()  # Retrieve all records from the database
    return render(request, 'view.records.html', 
                  {'record_list': record_list}) 