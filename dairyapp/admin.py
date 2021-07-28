from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(locations)
admin.site.register(Location)
admin.site.register(Notifications)
admin.site.register(Dailyrecords)

