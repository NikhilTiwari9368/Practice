from django.contrib import admin

from appointment.models import Appointment

class appointmentAdmin(admin.ModelAdmin):
    list_display = ('department', 'doctor' ,'name', 'email', 'appointment_date', 'appointment_time')

admin.site.register(Appointment, appointmentAdmin) 

# Register your models here.
