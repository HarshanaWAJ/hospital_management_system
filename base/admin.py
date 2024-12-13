from django.contrib import admin

# Import Models
from .models import Message


# Model Registration
admin.site.register(Message)