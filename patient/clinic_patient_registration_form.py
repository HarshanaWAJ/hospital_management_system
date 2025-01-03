from django import forms
from .models import ClinicPatient

class ClinicAdmittedPatientForm(forms.ModelForm):
    dob = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d', 
            attrs={'type': 'date',}
        )
    )
    
    class Meta:
        model = ClinicPatient
        fields = ['reg_id', 'first_name', 'last_name', 'dob', 'gender', 'contact_no', 'email', 'address', 'marital_status', 'address',
                  'clinic_reg_id', 'clinic_name', 'clinic_id', 'clinic_day']  # This will include all fields from the model
