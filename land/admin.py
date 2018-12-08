from django.contrib import admin
from .models import Let_Land, Lease_Let_Land, Request_To_Lease, Request_To_Lease_Offer, Sell_Land, Buy_Land, Request_To_Buy, Request_To_Buy_Offer

# Register your models here.

class LetLandInfoAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'owner_contact', 'land_size', 'region', 'price', 'price_per', 'available', 'lease_period')
    list_filter =  ('owner_name', 'owner_contact', 'land_size', 'region', 'price', 'price_per', 'available', 'water_source', 'lease_period', 'location')
    search_fields =  ('owner_name', 'owner_contact', 'land_size', 'region', 'price', 'price_per', 'available','water_source', 'lease_period', 'location')


class LeaseLetLandInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'lease_period', 'crop_to_grow', 'price', 'price_per', 'status')
    list_filter =  ('name', 'email', 'contact', 'lease_period', 'crop_to_grow', 'price', 'price_per', 'status')
    search_fields =  ('name', 'email', 'contact', 'lease_period', 'crop_to_grow', 'price', 'price_per', 'status')


class RequestToLeaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'land_size', 'region', 'price', 'price_per', 'lease_period')
    list_filter =  ('name', 'contact', 'land_size', 'region', 'price', 'price_per', 'lease_period')
    search_fields =  ('name', 'contact', 'land_size', 'region', 'price', 'price_per', 'lease_period')

class RequestToLeaseOfferInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'location', 'price', 'price_per', 'status')
    list_filter =  ('name', 'contact', 'location', 'price', 'price_per', 'status')
    search_fields =  ('name', 'contact', 'location', 'price', 'price_per', 'status')

class SellLandInfoAdmin(admin.ModelAdmin):
    list_display = ('land_size', 'region', 'price_range', 'price_per', 'owner_name', 'owner_contact', 'available')
    list_filter =  ('land_size', 'region', 'price_range', 'price_per', 'owner_name', 'owner_contact', 'available')
    search_fields =  ('land_size', 'region', 'price_range', 'price_per', 'owner_name', 'owner_contact', 'available')

class BuyLandInfoAdmin(admin.ModelAdmin):
    list_display = ('sell_land', 'price', 'price_per', 'name', 'contact')
    list_filter =  ('sell_land', 'price', 'price_per', 'name', 'contact')
    search_fields =  ('sell_land', 'price', 'price_per', 'name', 'contact')


class RequestToBuyInfoAdmin(admin.ModelAdmin):
    list_display = ('land_size', 'region', 'price_range', 'price_range_per', 'name','contact')
    list_filter =  ('land_size', 'region', 'price_range', 'price_range_per', 'name', 'contact')
    search_fields =  ('land_size', 'region', 'price_range', 'price_range_per', 'name', 'contact')


class RequestToBuyOfferInfoAdmin(admin.ModelAdmin):
    list_display = ('request_to_buy', 'name', 'contact', 'location', 'price', 'price_per', 'status')
    list_filter =  ('request_to_buy', 'name', 'contact', 'location', 'price', 'price_per', 'status')
    search_fields =  ('request_to_buy', 'name', 'contact', 'location', 'price', 'price_per', 'status')













admin.site.register(Let_Land, LetLandInfoAdmin)
admin.site.register(Lease_Let_Land, LeaseLetLandInfoAdmin)
admin.site.register(Request_To_Lease, RequestToLeaseInfoAdmin)
admin.site.register(Request_To_Lease_Offer, RequestToLeaseOfferInfoAdmin)
admin.site.register(Sell_Land, SellLandInfoAdmin)
admin.site.register(Buy_Land, BuyLandInfoAdmin)
admin.site.register(Request_To_Buy, RequestToBuyInfoAdmin)
admin.site.register(Request_To_Buy_Offer, RequestToBuyOfferInfoAdmin)

