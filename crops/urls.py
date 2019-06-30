from django.urls import path, include, re_path

from .views import all_crops_view, crop_detail_view


urlpatterns = [
    path('', all_crops_view, name="all-crops"),
    path('detail/<int:crop_id>', crop_detail_view, name="crop_detail"),
    



    
    
]