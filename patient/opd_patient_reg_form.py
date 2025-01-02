from django import forms
from .models import OPDPatient

class PatientForm(forms.ModelForm):
    class Meta:
        model = OPDPatient
        fields = ['reg_id', 'first_name', 'last_name', 'dob', 'gender', 'contact_no', 'email', 'address', 'marital_status', 'opd_reg_id', 'address']  # This will include all fields from the model
