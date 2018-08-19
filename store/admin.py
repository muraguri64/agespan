
from django.contrib import admin
from .models import Store_Product, Order

# Register your models here.

class StoreInfoAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'crop_type', 'quantity', 'units', 'unit_price', 'region', 'nearest_town', 'seller_name', 'seller_contact','seller_email')
    list_filter = ('product_name', 'region', 'crop_type', 'units', 'unit_price', 'quantity', 'seller_email', 'seller_contact')
    search_fields = ('product_name', 'crop_type',  'region', 'nearest_town', 'quantity', 'units', 'seller_name', 'seller_contact', 'seller_email')


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ('buyer_name', 'buyer_email', 'buyer_contact', 'quantity', 'units', 'unit_price', 'store_product')
    list_filter = ('buyer_name', 'buyer_email', 'buyer_contact', 'quantity', 'units', 'unit_price', 'store_product')
    search_fields = ('buyer_name', 'buyer_email', 'buyer_contact', 'quantity', 'units', 'unit_price', 'store_product')

   

admin.site.register(Store_Product, StoreInfoAdmin)
admin.site.register(Order, OrderInfoAdmin)


