from django.shortcuts import render
from .models import Message
from .contact_form import MessageForm


# Create views here.
def home(request):
    contact_form = MessageForm()

    if request.method == 'POST':
        print(request.post)

    context = {'contact_form': contact_form}
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def admin_message(request):
    admin_messages = Message.objects.all()
    context = {'admin_messages': admin_messages}
    return render(request, 'admin.message.html', context)