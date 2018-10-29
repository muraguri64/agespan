from django.contrib import admin
from .models import Register_Agrovet, Request_Product

# Register your models here.

class Register_Agrovet_Info_Admin(admin.ModelAdmin):
    list_display = ('agrovet_name','agrovet_contact', 'agrovet_email', 'region', 'location', 'nearest_town')
    list_filter = ('agrovet_name','agrovet_contact', 'agrovet_email', 'region', 'location', 'nearest_town')
    search_fields = ('agrovet_name','agrovet_contact', 'agrovet_email', 'region','location', 'nearest_town')

class Request_Product_Info_Admin(admin.ModelAdmin):
    list_display = ('requestor_name','requestor_contact', 'requestor_email',  'product_name', 'farm_name', 'region', 'delivery_location')
    list_filter = ('requestor_name','requestor_contact', 'requestor_email',  'product_name', 'farm_name', 'region', 'delivery_location')
    search_fields = ('requestor_name','requestor_contact', 'requestor_email',  'product_name', 'farm_name', 'region', 'delivery_location')


admin.site.register(Register_Agrovet, Register_Agrovet_Info_Admin)
admin.site.register(Request_Product, Request_Product_Info_Admin)
