from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    # Additional fields for registration
    title = forms.ChoiceField(
        required=False,
        choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss')],
        widget=forms.Select(attrs={'class': 'form-control form-control-lg'})
    )
    
    gender = forms.ChoiceField(
        required=False,
        choices=[('Male', 'Male'), ('Female', 'Female')],
        widget=forms.Select(attrs={'class': 'form-control form-control-lg'})
    )

    # Custom fields to override the default UserCreationForm fields
    dob = forms.DateField(
        required=False,
        widget=forms.DateInput(
            format='%Y-%m-%d', 
            attrs={'type': 'date', 'class': 'form-control'}
        )
    )
    street_address = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    street_name = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    postal_code = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    town = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    contact_no = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    country = forms.CharField(max_length=200, initial='Sri Lanka', disabled=True)
    emergency_contact_no = forms.CharField(max_length=200, required=False, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'title', 'gender', 'first_name', 'last_name', 'dob', 
                  'street_address', 'street_name', 'postal_code', 'town', 'contact_no', 
                  'emergency_contact_no']  

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Apply form control class to all fields
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control form-control-lg'})

    # Custom validation for email to check duplicate email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already registered')
        return email

    # Validate password matching
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2
