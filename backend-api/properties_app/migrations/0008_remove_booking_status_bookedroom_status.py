# Generated by Django 4.1.3 on 2022-11-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_app', '0007_remove_bookedroom_status_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.AddField(
            model_name='bookedroom',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
