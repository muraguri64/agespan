from django.contrib import admin
from .models import Region 

# Register your models here.

class regionInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

   

admin.site.register(Region, regionInfoAdmin)
