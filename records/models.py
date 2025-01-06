from django.db import models
from datetime import date

# Create your models here.
class record(models.Model):
    ref_no = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()

    date = models.DateField(default=date.today)

    medical_history = models.TextField(max_length=5000, blank=True)
    diagnosis = models.TextField(max_length=5000)
    treatment = models.TextField(max_length=5000)
    prescription = models.TextField(max_length=5000, blank=True)


    def __str__(self):
        return self.ref_no, date