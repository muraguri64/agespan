from django.urls import path, include, re_path

from .views import register_farm_view


urlpatterns = [
    path('register-farm/', register_farm_view, name="register-farm"),


    
    
]