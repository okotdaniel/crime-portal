from django.db import models
from datetime import datetime
# Create your models here.

class ReportSuspect(models.Model):
    locationList = (
        ('SBIT', 'SBIT'),
        ('SCIAD', 'SCIAD'),
        ('SLAW', 'SLAW'),
        ('Cafeteria', 'Cafeteria')
    )
    suspect_Name = models.CharField(max_length=30, null=True)
    Location = models.CharField(max_length=30, null=True, choices=locationList)
    Dress_Code = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.suspect_Name


class wantedSuspect(models.Model):
    genderList = (
        ('male', 'male'),
        ('female', 'female')
    )

    name = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    course = models.CharField(max_length=200, null=True)
    picture = models.ImageField(max_length=200, null=True)
    Dob = models.DateField(auto_now=False)
    Year_of_admission = models.CharField(max_length=200, null=True)
    Intake = models.CharField(max_length=200, null=True)
    Index_number = models.CharField(max_length=200, null=True)
    sex = models.CharField(choices=genderList, max_length=200)
    DatePosted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ReportCrimeModel(models.Model):
    pass


