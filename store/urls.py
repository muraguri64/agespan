from django.urls import path, include, re_path

from . import views


urlpatterns = [
    path('sellproduct/', views.sellproduct, name="sellproduct"),


    
    
]