from django.urls import path, include, re_path

from .views import sell_product_view


urlpatterns = [
    path('sellproduct/', sell_product_view, name="sellproduct"),


    
    
]