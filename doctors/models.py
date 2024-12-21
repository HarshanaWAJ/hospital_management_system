from django.db import models

from base.models import User
# Create your models here.

class Doctor(User):

    SPECIALTIES = [
        ('general', 'General'),
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('dermatology', 'Dermatology'),
        ('radiology', 'Radiology'),
        ('gastroenterology', 'Gastroenterology'),
        ('endocrinology', 'Endocrinology'),
        ('psychiatry', 'Psychiatry'),
        ('obstetrics', 'Obstetrics and Gynecology'),
        ('ophthalmology', 'Ophthalmology'),
        ('urology', 'Urology'),
        ('dentistry', 'Dentistry'),
        ('pulmonology', 'Pulmonology'),
        ('general_surgery', 'General Surgery'),
        ('emergency_medicine', 'Emergency Medicine'),
    ]

    DEGREES = [
        ('MBBS', 'MBBS'),
        ('MD', 'MD'),
        ('MS', 'MS'),
        ('BSc', 'BSc'),
        ('DNB', 'DNB'),
        ('DO', 'DO'),
        ('Fellowship', 'Fellowship'),
    ]

    # Degree field with choices for select dropdown
    degree = models.CharField(
        max_length=100,
        choices=DEGREES,
        blank=True,
        null=True
    )

    specialty = models.CharField(
        max_length=100,
        choices=SPECIALTIES,
        blank=True,
        null=True
    )
    years_of_experience = models.PositiveIntegerField()
    license_number = models.CharField(max_length=100)
    position = models.CharField(max_length=10, choices=[('Intern', 'Intern'), ('Doctor', 'Doctor'), ('Specialist', 'Specialist')], blank=True, null=True)

    # Override the save method to set is_user and is_doctor fields
    def save(self, *args, **kwargs):
        self.is_user = False  # Set is_user to False for Doctor
        self.is_doctor = True  # Set is_doctor to True for Doctor
        self.is_admin = False
        self.is_staff = False
        super().save(*args, **kwargs)  # Call the parent class's save method


    def __str__(self):
        return self.username