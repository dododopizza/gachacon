from django.contrib import admin
from .models import Profile, Info, Role

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'photo']

admin.site.register(Profile, ProfileAdmin)