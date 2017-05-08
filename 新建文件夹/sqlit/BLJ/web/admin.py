from django.contrib import admin

# Register your models here.
from web import models

admin.site.register(models.Host)
admin.site.register(models.HostGroups)
admin.site.register(models.IDC)
admin.site.register(models.UserProfile)
admin.site.register(models.HostToRemoteUser)
admin.site.register(models.RemoteUser)
admin.site.register(models.AuditLog)

