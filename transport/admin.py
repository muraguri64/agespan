from django.contrib import admin

from .models import Request_Transport, Request_Transport_Offer, Offer_Transport, Offer_Transport_Request

# Register your models here.

class Request_Transport_Info_Admin(admin.ModelAdmin):
    list_display = ('cargo_type','quantity_in_tones', 'means_of_transport', 'start_location', 'end_location', 'charges_per_km')
    list_filter = ('cargo_type','quantity_in_tones', 'means_of_transport', 'start_location', 'end_location', 'charges_per_km')
    search_fields = ('cargo_type','quantity_in_tones', 'means_of_transport', 'start_location', 'end_location', 'charges_per_km')


class Request_Transport_Offer_Info_Admin(admin.ModelAdmin):
    list_display = ('vehicle_number_plate','charges_per_km', 'offeror_name', 'offeror_contact','status')
    list_filter = ('vehicle_number_plate','charges_per_km','status')
    search_fields = ('vehicle_number_plate','charges_per_km','status', 'offeror_name', 'offeror_contact')

class Offer_Transport_Info_Admin(admin.ModelAdmin):
    list_display = ('vehicle_number_plate', 'vehicle_make', 'preferred_cargo', 'charges_per_km', 'offeror_name', 'offeror_contact')
    list_filter = ('vehicle_number_plate', 'vehicle_make', 'preferred_cargo', 'charges_per_km', 'offeror_name', 'offeror_contact')
    search_fields = ('vehicle_number_plate', 'vehicle_make', 'preferred_cargo', 'charges_per_km', 'offeror_name', 'offeror_contact')


class Offer_Transport_Request_Info_Admin(admin.ModelAdmin):
    list_display = ('cargo_type','quantity_in_tones', 'start_location', 'end_location', 'status')
    list_filter = ('cargo_type','quantity_in_tones', 'start_location', 'end_location', 'status')
    search_fields = ('cargo_type','quantity_in_tones', 'start_location', 'end_location','status')



admin.site.register(Request_Transport, Request_Transport_Info_Admin)
admin.site.register(Request_Transport_Offer, Request_Transport_Offer_Info_Admin)
admin.site.register(Offer_Transport, Offer_Transport_Info_Admin)
admin.site.register(Offer_Transport_Request, Offer_Transport_Request_Info_Admin)
