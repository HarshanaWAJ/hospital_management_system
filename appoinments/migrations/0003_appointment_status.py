# Generated by Django 5.1.4 on 2024-12-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoinments', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]
