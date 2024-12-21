# Generated by Django 5.1.4 on 2024-12-21 11:48

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(blank=True, choices=[('Intern', 'Intern'), ('Nurse', 'Nurse'), ('Registered Nurse', 'Registered Nurse'), ('Licensed Practical Nurse', 'Licensed Practical Nurse'), ('Physician Assistant', 'Physician Assistant'), ('Nurse Practitioner', 'Nurse Practitioner'), ('Medical Technologist', 'Medical Technologist'), ('Laboratory Technician', 'Laboratory Technician'), ('Radiologic Technologist', 'Radiologic Technologist'), ('Phlebotomist', 'Phlebotomist'), ('Pharmacist', 'Pharmacist'), ('Pharmacy Technician', 'Pharmacy Technician'), ('Physical Therapist', 'Physical Therapist'), ('Occupational Therapist', 'Occupational Therapist'), ('Social Worker', 'Social Worker'), ('Dietitian', 'Dietitian'), ('Medical Records Technician', 'Medical Records Technician'), ('Health Information Technician', 'Health Information Technician'), ('Respiratory Therapist', 'Respiratory Therapist'), ('Housekeeping', 'Housekeeping'), ('Sterile Processing Technician', 'Sterile Processing Technician'), ('EMT', 'EMT'), ('Paramedic', 'Paramedic'), ('Patient Care Technician', 'Patient Care Technician'), ('Surgical Technologist', 'Surgical Technologist'), ('IT Support', 'IT Support'), ('Security Officer', 'Security Officer'), ('Chaplain', 'Chaplain'), ('Transporter', 'Transporter'), ('Logistics Coordinator', 'Logistics Coordinator')], max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('base.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
