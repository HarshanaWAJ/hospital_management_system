from django import forms
from .models import Staff

class StaffRegForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'})
    )
    dob = forms.DateField(
        required=False,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date', 'class': 'form-control form-control-lg'}
        )
    )

    class Meta:
        model = Staff
        fields = ['username', 'email', 'title', 'gender', 'first_name', 'last_name', 'dob', 
                  'street_address', 'street_name', 'postal_code', 'town', 'contact_no', 
                  'emergency_contact_no', 'password', 'position']

    def save(self, commit=True):
        # Get the instance (which could be new or existing)
        instance = super().save(commit=False)

        # Hash the password using Django's set_password method
        instance.set_password(self.cleaned_data['password'])

        # Save the instance if commit is True
        if commit:
            instance.save()

        return instance
