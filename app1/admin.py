from django.contrib import admin
from .models import Registration,Location,Weather
# Register your models here.

admin.site.register(Registration)
admin.site.register(Location)
admin.site.register(Weather)