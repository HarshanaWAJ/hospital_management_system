from django.shortcuts import render, redirect
from .staff_reg_form import StaffRegForm
from .models import Staff

# Create your views here.
def register_staff(request):
    if request.method == 'POST':
        form = StaffRegForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data (creates a new Doctor instance)
            return redirect('staff_management')  # Redirect after successful form submission
        else:
            # Print form errors if form is not valid
            print("Form is not valid!")
            print(form.errors)  # This will print the error dictionary to the console
    else:
        form = StaffRegForm()  # Create an empty form instance

    return render(request, 'staff.registration.html', {'form': form})


# Staff Management Page View
def staff_management(request):
    staff_list = Staff.objects.all()
    return render(request, 'staff.management.html', {
        'staff_list': staff_list
    })