from django.contrib import admin

from accounts.models import City, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(City)