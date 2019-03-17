from django.contrib import admin
from .models import Market

# Register your models here.

class MarketInfoAdmin(admin.ModelAdmin):
    list_display = ('crop_type', 'region')
    list_filter = ('crop_type', 'region')
    search_fields = ('crop_type', 'region')   

admin.site.register(Market, MarketInfoAdmin)


