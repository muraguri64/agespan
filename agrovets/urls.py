from django.urls import path, include, re_path

from .views import register_agrovet_view, all_agrovets_view, request_product_view, all_requested_products_view, agrovet_detail_view


urlpatterns = [
    path('register-agrovet/', register_agrovet_view, name="register-agrovet"),
    path('all-agrovets/', all_agrovets_view, name="all-agrovets"),
    path('request-product/', request_product_view, name="request-product"),
    path('all-requested-products/', all_requested_products_view, name="all-requested-products"),
    path('detail/<int:agrovet_id>', agrovet_detail_view, name="agrovet_detail"),



    
    
]