from django.shortcuts import render, redirect
from .admin_reg_form import SiteAdminForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import SiteAdmin

@login_required
def register_admin(request):
    if request.method == 'POST':  # POST request to handle form submission
        form = SiteAdminForm(request.POST)  
        if form.is_valid():
            form.save()  # Save the form data
            return redirect('admin_management')  # Redirect to another page after successful form submission
        else:
            print("Form is not valid!")
            print(form.errors)
            return render(request, 'admin.register.html', {'form': form})
    else:
        form = SiteAdminForm()  # Empty form for GET request
    return render(request, 'admin.register.html', {'form': form})


@login_required
def admin_management(request):
    admin_list = SiteAdmin.objects.all()
    return render(request, 'admin.management.html', {
        'admin_list': admin_list
    })

@login_required
def delete_admin(request, id):
    admin = SiteAdmin.objects.get(id=id)
    admin.delete()
    return redirect('admin_management')


def get_admin_data(request, admin_id):
    admin = get_object_or_404(SiteAdmin, id=admin_id)

    print(admin)
    
    # Return admin data in JSON format
    data = {
        'admin': {
            'id': admin.id,
            'title': admin.title,
            'first_name': admin.first_name,
            'last_name': admin.last_name,
            'gender': admin.gender,
            'email': admin.email,
            'dob': admin.dob,
            'street_address': admin.street_address,
            'street_name': admin.street_name,
            'town': admin.town,
            'postal_code': admin.postal_code,
            'contact_no': admin.contact_no,
            'emergency_contact_no': admin.emergency_contact_no,
        }
    }
    return JsonResponse(data)