from django.contrib import admin
from .models import Register_Agronomist, Register_Agronomist_Request, Request_Agronomist, Request_Agronomist_Offer

# Register your models here.

class Register_Agronomist_Info_Admin(admin.ModelAdmin):
    list_display = ('agronomist_name','agronomist_contact', 'agronomist_email', 'crop_type', 'region')
    list_filter = ('agronomist_name','agronomist_contact', 'agronomist_email', 'crop_type', 'region')
    search_fields = ('agronomist_name','agronomist_contact', 'agronomist_email', 'crop_type', 'region')

class Register_Agronomist_Request_Info_Admin(admin.ModelAdmin):
    list_display = ('requestor_name','requestor_contact', 'requestor_email',  'location', 'status')
    list_filter = ('requestor_name','requestor_contact', 'requestor_email',  'location', 'status')
    search_fields = ('requestor_name','requestor_contact', 'requestor_email',  'location', 'status')

class Request_Agronomist_Info_Admin(admin.ModelAdmin):
    list_display = ('requestor_name','requestor_contact', 'requestor_email',  'crop_type', 'region', 'location')
    list_filter = ('requestor_name','requestor_contact', 'requestor_email',  'crop_type', 'region', 'location')
    search_fields = ('requestor_name','requestor_contact', 'requestor_email',  'crop_type', 'region', 'location')

class Request_Agronomist_Offer_Info_Admin(admin.ModelAdmin):
    list_display = ('offeror_name','offeror_contact', 'offeror_email',  'status')
    list_filter = ('offeror_name','offeror_contact', 'offeror_email',  'status')
    search_fields = ('offeror_name','offeror_contact', 'offeror_email',  'status')

admin.site.register(Register_Agronomist, Register_Agronomist_Info_Admin)
admin.site.register(Register_Agronomist_Request, Register_Agronomist_Request_Info_Admin)
admin.site.register(Request_Agronomist, Request_Agronomist_Info_Admin)
admin.site.register(Request_Agronomist_Offer, Request_Agronomist_Offer_Info_Admin)




