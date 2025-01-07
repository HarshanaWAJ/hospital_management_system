from django import forms
from .models import Record
from datetime import date

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'  # Include all fields except 'date' (it's hidden)

    def save(self, commit=True):
        # Set the date field to today's date if it is not provided
        if not self.cleaned_data.get('date'):
            self.cleaned_data['date'] = date.today()

        return super().save(commit)
