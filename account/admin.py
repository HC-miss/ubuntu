from django.contrib import admin
from .models import *


class UserSite(admin.ModelAdmin):
    list_display = ['id', 'user', 'telephone', 'org', 'create_time', 'mod_date']


admin.site.register(UserProfile, UserSite)
