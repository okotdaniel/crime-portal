from django.contrib import admin

# Register your models here.


from django.contrib import admin
from . import models 

admin.site.register(models.ReportSuspect)
admin.site.register(models.wantedSuspect)
