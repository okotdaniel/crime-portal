from django.contrib import admin
from administrator.models import Contacts, Announcements,Tips

# Register your models here.
admin.site.register(Contacts)
admin.site.register(Announcements)
admin.site.register(Tips)