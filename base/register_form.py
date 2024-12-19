from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    
    dob = forms.DateField(
    required=False,
    widget=forms.DateInput(
        format='%Y-%m-%d',  # Use this format to match the expected input format for the HTML date input
        attrs={'type': 'date', 'class': 'form-control'}  # 'type': 'date' ensures it uses the HTML5 date picker
        )
    )
    first_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    street_address = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    street_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    postal_code = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    town = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    contact_no = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    emergency_contact_no = forms.CharField(max_length=200, required=True, widget=forms.TextInput())
    # Password fields
    password1 = forms.CharField(max_length=200, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=200, required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'title', 'gender', 
                  'dob', 'street_address', 'street_name', 'postal_code', 'town', 'country', 'contact_no', 
                  'emergency_contact_no']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Apply form control class to all fields
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control form-control-lg'})

    # Custom validation for password1
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        return password1

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
