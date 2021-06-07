from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from django.contrib import admin

from .models import *

admin.site.site_header = 'Medico Consultation Admin Panel'

admin.site.register(Doctor)

admin.site.register(TakeAppointment)
admin.site.register(Department)
admin.site.register(MeetLink)
