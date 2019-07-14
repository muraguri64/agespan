from django.urls import path, include, re_path

from .views import register_farm_view, all_farms_view, farm_detail_view


urlpatterns = [
    path('register-farm/', register_farm_view, name="register-farm"),
    path('all-farms/', all_farms_view, name="all-farms"),
    path('detail/<int:farm_id>', farm_detail_view, name="farm_detail"),


    
    
]