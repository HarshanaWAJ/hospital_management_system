from base.models import User
from django.db import models

# Create your models here.
class Staff(User):
    exclude = ['date_joined']

    POSITION_CHOICES = [
        ('Intern', 'Intern'),
        ('Nurse', 'Nurse'),
        ('Registered Nurse', 'Registered Nurse'),
        ('Licensed Practical Nurse', 'Licensed Practical Nurse'),
        ('Physician Assistant', 'Physician Assistant'),
        ('Nurse Practitioner', 'Nurse Practitioner'),
        ('Medical Technologist', 'Medical Technologist'),
        ('Laboratory Technician', 'Laboratory Technician'),
        ('Radiologic Technologist', 'Radiologic Technologist'),
        ('Phlebotomist', 'Phlebotomist'),
        ('Pharmacist', 'Pharmacist'),
        ('Pharmacy Technician', 'Pharmacy Technician'),
        ('Physical Therapist', 'Physical Therapist'),
        ('Occupational Therapist', 'Occupational Therapist'),
        ('Social Worker', 'Social Worker'),
        ('Dietitian', 'Dietitian'),
        ('Medical Records Technician', 'Medical Records Technician'),
        ('Health Information Technician', 'Health Information Technician'),
        ('Respiratory Therapist', 'Respiratory Therapist'),
        ('Housekeeping', 'Housekeeping'),
        ('Sterile Processing Technician', 'Sterile Processing Technician'),
        ('EMT', 'EMT'),
        ('Paramedic', 'Paramedic'),
        ('Patient Care Technician', 'Patient Care Technician'),
        ('Surgical Technologist', 'Surgical Technologist'),
        ('IT Support', 'IT Support'),
        ('Security Officer', 'Security Officer'),
        ('Chaplain', 'Chaplain'),
        ('Transporter', 'Transporter'),
        ('Logistics Coordinator', 'Logistics Coordinator'),
    ]

    position = models.CharField(max_length=50, choices=POSITION_CHOICES, blank=True, null=True)
    
    # Override the save method to set is_user and is_doctor fields
    def save(self, *args, **kwargs):
        self.is_user = False  # Set is_user to False for Admin
        self.is_doctor = False  # Set is_doctor to False for Admin
        self.is_admin = False    # Set is_admin to True for Admin
        self.is_staff = True   # Set is_staff to False for Admin
        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.username