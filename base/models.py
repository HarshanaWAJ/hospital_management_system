from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Message Model
class Message(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 300)
    message = models.TextField(null=False, blank = False)
    update_at = models.DateTimeField(auto_now = True) # Get the Date & Tome Data Updated
    created_at = models.DateTimeField(auto_now_add = True) # Save the Time and Date that the record saved


    def __str__(self):
        return self.name


# User Model
class User(AbstractUser):
    # Additional fields to match the form data
    title = models.CharField(max_length=10, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss')], blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, default='Sri Lanka', blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact_no = models.CharField(max_length=15, blank=True, null=True)
    # For user authentication, the default email/password from AbstractUser will suffice

    is_admin = models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=True)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_staff = models.BooleanField('Is staff', default=False)

    def __str__(self):
        return self.username