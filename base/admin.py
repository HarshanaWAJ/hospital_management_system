from django.contrib import admin

# Import Models
from .models import Message
from .models import User


# Model Registration
admin.site.register(Message)
admin.site.register(User)