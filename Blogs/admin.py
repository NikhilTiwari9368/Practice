from django.contrib import admin

# Register your models here.
from Blogs.models import BlogPost 

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image','video' ,'content')
    
admin.site.register(BlogPost, BlogAdmin)  