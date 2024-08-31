
from django.contrib import admin

# Register your models here.
from Precaution.models import Disease

# Admin interface for the Disease model
@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name','description','precautions','what_to_eat','daily_exercise','instructions','image','treatment','medicine','video')
    
# Admin interface for the Video model

    
    
    