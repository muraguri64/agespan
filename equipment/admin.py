from django.contrib import admin
from .models import Equipment_Type, Let_Equipment, Hire_Equipment, Sell_Equipment, Buy_Equipment

# Register your models here.

class EquipmentTypeInfoAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name',)
    search_fields = ('name','description')



class LetEquipmentInfoAdmin(admin.ModelAdmin):
    list_display = ('equipment_name', 'equipment_type', 'manufacture_year', 'region', 'price', 'price_per', 'owner_name', 'owner_contact')
    list_filter =  ('equipment_name', 'equipment_type', 'manufacture_year', 'region', 'price', 'price_per')
    search_fields =  ('equipment_name', 'equipment_type', 'manufacture_year', 'region', 'price', 'price_per', 'owner_name', 'owner_contact')


class HireEquipmentInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'farm_size', 'farm_location', 'price', 'price_per', 'status')
    list_filter =  ('name', 'email', 'contact', 'farm_size', 'farm_location', 'price', 'price_per', 'status')
    search_fields =  ('name', 'email', 'contact', 'farm_size', 'farm_location', 'price', 'price_per', 'status')


class SellEquipmentInfoAdmin(admin.ModelAdmin):
    list_display = ('equipment_name', 'equipment_type', 'manufacture_year', 'region', 'price_range_from', 'price_range_to', 'owner_name', 'owner_contact')
    list_filter =  ('equipment_name', 'equipment_type', 'manufacture_year', 'region', 'price_range_from', 'price_range_to')
    search_fields =  ('equipment_name', 'equipment_type', 'manufacture_year', 'region', 'price_range_from', 'price_range_to', 'owner_name', 'owner_contact')

class BuyEquipmentInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'price_to_buy', 'status')
    list_filter =  ('name', 'email', 'contact', 'price_to_buy', 'status')
    search_fields =  ('name', 'email', 'contact', 'price_to_buy', 'status')



admin.site.register(Equipment_Type, EquipmentTypeInfoAdmin)
admin.site.register(Let_Equipment, LetEquipmentInfoAdmin)
admin.site.register(Hire_Equipment, HireEquipmentInfoAdmin)
admin.site.register(Sell_Equipment, SellEquipmentInfoAdmin)
admin.site.register(Buy_Equipment, BuyEquipmentInfoAdmin)

