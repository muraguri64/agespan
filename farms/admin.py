from django.contrib import admin
from .models import Register_Farm

# Register your models here.

class registerFarmInfoAdmin(admin.ModelAdmin):
    list_display = ('farm_name', 'farm_size', 'location', 'nearest_town', 'planting_date', 'crop_grown', 'region', 'user')
    list_filter = ('farm_name', 'farm_size', 'location', 'nearest_town', 'planting_date', 'crop_grown', 'region', 'user')
    search_fields = ('farm_name', 'farm_size', 'location', 'nearest_town', 'planting_date', 'crop_grown', 'region', 'user')

   

admin.site.register(Register_Farm, registerFarmInfoAdmin)
