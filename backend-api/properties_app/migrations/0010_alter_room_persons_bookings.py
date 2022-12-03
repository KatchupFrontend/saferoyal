# Generated by Django 4.1.3 on 2022-11-29 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties_app', '0009_rename_booking_book_delete_bookedroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='persons',
            field=models.CharField(choices=[('1 in 1', 'one in one'), ('2 in 1', 'Two in one'), ('3 in 1', 'Three in one'), ('4 in 1', 'Four in one')], max_length=100),
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties_app.book')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties_app.room')),
            ],
        ),
    ]
