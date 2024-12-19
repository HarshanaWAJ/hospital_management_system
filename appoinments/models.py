from django.db import models

class Appointment(models.Model):
    GENDER_CHOICES = [
        ('', 'Select One'),  # Disabled default option
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    DEPARTMENT_CHOICES = [
        ('', 'Select One'),  # Disabled default option
        ('OPD', 'OPD'),
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Other', 'Other'),
        # Add other departments here
    ]

    patient_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(blank=True, null=True)
    appointment_date = models.DateTimeField()
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    reason_for_appointment = models.TextField()
    appointment_type = models.CharField(max_length=50, choices=[('Consultation', 'Consultation'), ('Follow-up', 'Follow-up'), ('Emergency', 'Emergency')])
    symptoms = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    referring_doctor = models.CharField(max_length=100, blank=True, null=True)
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    policy_number = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=200, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    language_preference = models.CharField(max_length=50, blank=True, null=True)
    special_requirements = models.TextField(blank=True, null=True)
    consent_for_treatment = models.BooleanField(default=False)
    data_privacy_agreement = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient_name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}"
