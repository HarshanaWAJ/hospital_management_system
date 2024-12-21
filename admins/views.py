from django.shortcuts import render, redirect
from .admin_reg_form import SiteAdminForm

def register_admin(request):
    if request.method == 'POST':  # POST request to handle form submission
        form = SiteAdminForm(request.POST)  
        if form.is_valid():
            form.save()  # Save the form data
            return redirect('admin_list')  # Redirect to another page after successful form submission
        else:
            print("Form is not valid!")
            print(form.errors)
            return render(request, 'admin.register.html', {'form': form})
    else:
        form = SiteAdminForm()  # Empty form for GET request
    return render(request, 'admin.register.html', {'form': form})
