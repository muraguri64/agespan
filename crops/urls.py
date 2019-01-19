from django.urls import path, include, re_path

from .views import all_crops_view


urlpatterns = [
    path('', all_crops_view, name="all-crops"),
    



    
    
]