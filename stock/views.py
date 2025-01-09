from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Stock, Supplier

@login_required
def view_stock_dashboard(request):
    """Get The Data List"""
    
    # Check if the user is an instance of Staff and is a Pharmacist
    if not hasattr(request.user, 'staff') or request.user.staff.position != 'Pharmacist':
        # Send a toast message and redirect to staff_dashboard if not authorized
        messages.error(request, "You are not authorized to access stocks.")
        return redirect('staff_dashboard')  # Adjust the URL name for staff_dashboard if necessary
    
    # If the user is a Pharmacist, proceed with fetching stock and supplier data
    stocks = Stock.objects.all()
    suppliers = Supplier.objects.all()

    # Render the stock dashboard
    return render(request, 'stock.dashboard.html', {
        'stocks': stocks,
        'suppliers': suppliers,
        'user': request.user  # Explicitly passing the user object to the template
    })

