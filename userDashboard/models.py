from django.db import models
from datetime import datetime
# Create your models here.
class contacts(models.Model):
    profession = (
        ('Student','student'),
        ('Lecturer','Lecturer'),
        ('Security','Security'),
        ('Administrator','Administrator')
    )

    Names = models.CharField(max_length=30, null=True)
    Phone = models.CharField(max_length=30, null=True)
    Profession = models.CharField(max_length=30, null=True,  choices=profession )
    Calling_hours = models.CharField(max_length=20, null=True)
    Comments = models.TextField(max_length=200, null=True)
    Date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Names

class tips(models.Model):
    Title = models.CharField(max_length=30, null=True) 
    Details = models.TextField(max_length=200, null=True)
    DatePosted = models.DateTimeField(auto_now=True, null=True)
    UserProfession = models.TextField(max_length=200, null=True, choices=contacts.profession)

    def __str__(self):
        return self.Title

class reportSuspect(models.Model):
    locationList = (
        ('SBIT', 'SBIT'),
        ('SCIAD', 'SCIAD'),
        ('SLAW', 'SLAW'),
        ('Cafeteria', 'Cafeteria')
    )    
    suspect_Name = models.CharField(max_length=30, null=True)
    Location = models.CharField(max_length=30, null=True, choices =locationList)
    Dress_Code = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.suspect_Name


