# Generated by Django 5.1.4 on 2024-12-23 05:43

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
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('degree', models.CharField(blank=True, choices=[('MBBS', 'MBBS'), ('MD', 'MD'), ('MS', 'MS'), ('BSc', 'BSc'), ('DNB', 'DNB'), ('DO', 'DO'), ('Fellowship', 'Fellowship')], max_length=100, null=True)),
                ('specialty', models.CharField(blank=True, choices=[('general', 'General'), ('cardiology', 'Cardiology'), ('neurology', 'Neurology'), ('pediatrics', 'Pediatrics'), ('orthopedics', 'Orthopedics'), ('dermatology', 'Dermatology'), ('radiology', 'Radiology'), ('gastroenterology', 'Gastroenterology'), ('endocrinology', 'Endocrinology'), ('psychiatry', 'Psychiatry'), ('obstetrics', 'Obstetrics and Gynecology'), ('ophthalmology', 'Ophthalmology'), ('urology', 'Urology'), ('dentistry', 'Dentistry'), ('pulmonology', 'Pulmonology'), ('general_surgery', 'General Surgery'), ('emergency_medicine', 'Emergency Medicine')], max_length=100, null=True)),
                ('years_of_experience', models.PositiveIntegerField()),
                ('license_number', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, choices=[('Intern', 'Intern'), ('Doctor', 'Doctor'), ('Specialist', 'Specialist')], max_length=10, null=True)),
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