from django.db import models

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
