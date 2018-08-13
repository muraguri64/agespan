from django.contrib import admin
from .models import Crop_Type 

# Register your models here.

class cropTypeInfoAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name',)
    search_fields = ('name','description')

   

admin.site.register(Crop_Type, cropTypeInfoAdmin)
