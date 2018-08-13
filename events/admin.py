
from django.contrib import admin
from .models import Event

# Register your models here.

class EventInfoAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'location',  'region', 'nearest_town', 'start_date', 'end_date', 'organizer_name', 'organizer_contact')
    list_filter = ('event_name', 'region', 'start_date', 'end_date', 'organizer_name', 'organizer_contact')
    search_fields = ('event_name', 'location',  'region', 'nearest_town', 'start_date', 'end_date', 'organizer_name', 'organizer_contact')

   

admin.site.register(Event, EventInfoAdmin)


