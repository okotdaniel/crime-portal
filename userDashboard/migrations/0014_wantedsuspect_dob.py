# Generated by Django 3.0.8 on 2020-10-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDashboard', '0013_wantedsuspect_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='wantedsuspect',
            name='Dob',
            field=models.DateField(auto_now=True),
        ),
    ]
