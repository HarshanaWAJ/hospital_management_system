# Generated by Django 5.1.4 on 2025-01-03 04:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_admittedpatient_discharge_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicpatient',
            name='registered_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
