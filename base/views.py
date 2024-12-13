from django.shortcuts import render, redirect
from .models import Message
from .contact_form import MessageForm
from django.urls import reverse



# Create views here.
def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to home page with success query parameter
            return redirect(f"{reverse('home')}?success=true")
        else:
            # Redirect to home page with error query parameter
            return redirect(f"{reverse('home')}?error=true")
    else:
        form = MessageForm()
    return render(request, 'home.html', {'contact_form': form})


# Login
def login(request):
    return render(request, 'login.html')

# Register
def register(request):
    return render(request, 'register.html')

# Admin Messages
def admin_message(request):
    admin_messages = Message.objects.all()
    context = {'admin_messages': admin_messages}
    return render(request, 'admin.message.html', context)