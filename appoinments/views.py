from django.shortcuts import render

# Create your views here.
def make_appoinment(request):
    return render(request, 'make.appoinments.html')