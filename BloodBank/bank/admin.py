from django.contrib import admin
from .models import UserProfile,BloodStock

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BloodStock)