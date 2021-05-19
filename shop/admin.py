from django.contrib import admin

from .models import Product, Phone
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display =['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Product, ProductAdmin)
admin.site.register(Phone, PhoneAdmin)

