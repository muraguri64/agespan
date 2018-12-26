from django.urls import path, include, re_path

from .views import register_agrovet_view


urlpatterns = [
    path('register-agrovet/', register_agrovet_view, name="register-agrovet"),
    #path('all-agrovet/', all_farms_view, name="all-farms"),


    
    
]