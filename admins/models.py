from base.models import User

class SiteAdmin(User):
    # Override the save method to set is_user and is_doctor fields
    def save(self, *args, **kwargs):
        self.is_user = False  # Set is_user to False for Admin
        self.is_doctor = False  # Set is_doctor to False for Admin
        self.is_admin = True    # Set is_admin to True for Admin
        self.is_staff = False   # Set is_staff to False for Admin
        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.username
