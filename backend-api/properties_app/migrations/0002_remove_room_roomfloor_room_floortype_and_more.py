# Generated by Django 4.1.3 on 2022-11-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='roomFloor',
        ),
        migrations.AddField(
            model_name='room',
            name='floortype',
            field=models.CharField(choices=[('1st', 'First'), ('2nd', 'Second')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FloorCategory',
        ),
    ]