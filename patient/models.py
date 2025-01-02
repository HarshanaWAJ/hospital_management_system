from django.db import models

class Patient(models.Model):
    reg_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(
        max_length=6, 
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )
    contact_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    address = models.TextField()
    marital_status = models.CharField(
        max_length=10, 
        choices=[('Single', 'Single'), ('Married', 'Married'), 
                 ('Divorced', 'Divorced'), ('Widowed', 'Widowed')]
    )

    # This is an abstract base class, so Django will not create a table for it
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.reg_id}"


class OPDPatient(Patient):
     opd_reg_id = models.CharField(max_length=100, unique=True)
     def __str__(self):
        return f"{self.reg_id}"
     


class ClinicPatient(Patient):
    clinic_reg_id = models.CharField(max_length=100, unique=True)
    clinic_name = models.CharField(max_length=100)
    clinic_id = models.CharField(max_length=100)
    clinic_day = models.CharField(max_length=100,choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), 
                                            ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
                                            ('Friday', 'Friday'), ('Saturday', 'Saturday'),
                                            ('Sunday', 'Sunday')])

    def __str__(self):
        return f"{self.reg_id} {self.clinic_reg_id}"
    

class AdmittedPatient(Patient):
    admission_no = models.CharField(max_length=100, unique=True)
    admission_date = models.DateField()
    discharge_date = models.DateField()
    room_no = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=10)
    ward_no = models.CharField(max_length=10)
    status = models.CharField(
        max_length=10, 
        choices=[('Admitted', 'Admitted'), ('Discharged', 'Discharged')],
        default='Admitted'
    )

    def __str__(self):
        return f"{self.reg_id} {self.admission_no}"