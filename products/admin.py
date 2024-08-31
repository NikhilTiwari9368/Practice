from django.contrib import admin

# Register your models here.
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description' ,'price','image','usage')
    
admin.site.register(Product, ProductAdmin) 