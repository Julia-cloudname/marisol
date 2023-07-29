# Generated by Django 3.2.20 on 2023-07-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('details', models.TextField(blank=True)),
                ('call_date', models.DateField()),
                ('call_time', models.TimeField()),
                ('enabled_dates', models.DateField()),
                ('disabled_dates', models.DateField()),
                ('enable_time', models.TimeField()),
                ('disable_time', models.TimeField()),
            ],
        ),
    ]
