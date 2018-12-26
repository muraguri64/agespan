from django.urls import path, include, re_path

from .views import register_agrovet_view, all_agrovets_view


urlpatterns = [
    path('register-agrovet/', register_agrovet_view, name="register-agrovet"),
    path('all-agrovets/', all_agrovets_view, name="all-agrovets"),


    
    
]