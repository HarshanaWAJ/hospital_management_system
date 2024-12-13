from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .contact_form import MessageForm
from django.urls import reverse
from django.http import JsonResponse



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

# Delete Message View
def delete_message(request, message_id):
    if request.method == 'POST' and request.is_ajax():
        try:
            print(message_id)
            # Get the message by ID
            message = get_object_or_404(Message, id=message_id)
            
            # Delete the message
            message.delete()

            # Return a JSON response indicating success
            return JsonResponse({'message': 'Success'})
        
        except Message.DoesNotExist:
            return JsonResponse({'message': 'Error: Message not found'}, status=404)
    
    # Return error if not an AJAX request or if the method is not POST
    return JsonResponse({'message': 'Error: Invalid request'}, status=400)


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