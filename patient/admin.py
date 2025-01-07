from django.contrib import admin
from .models import ClinicPatient, AdmittedPatient, OPDPatient

# Register your models here.

admin.site.register(ClinicPatient)
admin.site.register(AdmittedPatient)
admin.site.register(OPDPatient)

