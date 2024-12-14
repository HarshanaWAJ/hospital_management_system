from django.db import models

# Create your models here.

# Appoinment Model
class Appointment(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_id = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(blank=True, null=True)
    
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    # doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
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
        return self.name