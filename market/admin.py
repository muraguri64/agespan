from django.contrib import admin
from .models import Market, Graph_Data

# Register your models here.

class MarketInfoAdmin(admin.ModelAdmin):
    list_display = ('crop_type', 'region')
    list_filter = ('crop_type', 'region')
    search_fields = ('crop_type', 'region')  

class Graph_Data_Info_Admin(admin.ModelAdmin):
    list_display = ('market', 'date', 'price')
    list_filter = ('market', 'date', 'price')
    search_fields = ('market', 'date', 'price') 

admin.site.register(Market, MarketInfoAdmin)
admin.site.register(Graph_Data, Graph_Data_Info_Admin)


