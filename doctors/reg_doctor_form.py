from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    dob = forms.DateField(
        required=False,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date', 'class': 'form-control'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'})
    )

    class Meta:
        model = Doctor
        fields = [
            'username', 'password', 'title', 'gender', 'first_name', 'last_name', 'dob', 'email',
            'street_address', 'street_name', 'postal_code', 'town', 'country',
            'contact_no', 'emergency_contact_no', 'degree','specialty', 'years_of_experience', 'license_number',
            'position'
        ]

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': field.label
            })

            if isinstance(field.widget, forms.DateInput):
                field.widget.attrs.update({'type': 'date'})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})

    def save(self, commit=True):
        # Ensure password is hashed before saving
        doctor = super(DoctorForm, self).save(commit=False)

        # Hash password if it's provided
        if self.cleaned_data.get('password'):
            doctor.set_password(self.cleaned_data['password'])
        
        if commit:
            doctor.save()
        
        return doctor
