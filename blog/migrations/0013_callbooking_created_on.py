# Generated by Django 3.2.20 on 2023-08-05 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_callbooking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbooking',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]