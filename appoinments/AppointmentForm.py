from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    # Customizing widgets for specific fields

    # Date of Birth - Use 'date' type widget
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # Appointment Date - Use 'datetime-local' type widget
    appointment_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    # Phone Number - Use 'tel' type widget
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    
    # Emergency Contact Phone - Use 'tel' type widget
    emergency_contact_phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
