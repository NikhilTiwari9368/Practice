from django.contrib import admin

from Contactus.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','message')
    
admin.site.register(Contact, ContactAdmin) 

# Register your models here.