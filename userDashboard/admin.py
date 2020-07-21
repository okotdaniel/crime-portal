from django.contrib import admin
from . import models 

admin.site.register(models.contacts)
admin.site.register(models.tips)
admin.site.register(models.reportSuspect)
admin.site.register(models.wantedSuspect)
