# Generated by Django 3.2.20 on 2023-07-31 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230730_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbooking',
            name='booked_time_slots',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='callbooking',
            name='client_name',
            field=models.CharField(max_length=50),
        ),
    ]