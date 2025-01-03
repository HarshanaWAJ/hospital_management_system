from django.db import models

class Patient(models.Model):
    reg_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=6, choices=gender_choices)
    contact_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    marital_status_choices = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed')
    ]
    marital_status = models.CharField(
        max_length=10, 
        choices=marital_status_choices
    )

    # This is an abstract base class, so Django will not create a table for it
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.reg_id} - {self.first_name} {self.last_name}"


class OPDPatient(Patient):
    opd_reg_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"OPD: {self.reg_id} ({self.first_name} {self.last_name})"


class ClinicPatient(Patient):
    clinic_reg_id = models.CharField(max_length=100, unique=True)
    clinic_name = models.CharField(max_length=100)
    clinic_id = models.CharField(max_length=100)
    clinic_day_choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('All Days', 'All Days')
    ]
    clinic_day = models.CharField(max_length=100, choices=clinic_day_choices, default='All Days')

    def __str__(self):
        return f"Clinic: {self.reg_id} {self.clinic_name}"


class AdmittedPatient(Patient):
    admission_no = models.CharField(max_length=100, unique=True)
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)
    room_no = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=10)
    ward_no = models.CharField(max_length=10)
    status_choices = [
        ('Admitted', 'Admitted'),
        ('Discharged', 'Discharged')
    ]
    status = models.CharField(
        max_length=10, 
        choices=status_choices,
        default='Admitted'
    )

    def __str__(self):
        return f"Admitted: {self.reg_id} {self.admission_no}"
