from django import forms
from .models import AdmittedPatient

class AdmittedPatientForm(forms.ModelForm):
    dob = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d', 
            attrs={'type': 'date',}
        )
    )
    admission_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d', 
            attrs={'type': 'date',}
        )
    )
    
    class Meta:
        model = AdmittedPatient
        fields = ['reg_id', 'first_name', 'last_name', 'dob', 'gender', 'contact_no', 'email', 'address', 'marital_status', 'address',
                  'admission_no', 'admission_date', 'room_no', 'bed_no', 'ward_no']  # This will include all fields from the model
