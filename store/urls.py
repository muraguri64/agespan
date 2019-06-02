from django.urls import path, include, re_path

from .views import sell_product_view, store_products_view, product_detail_view


urlpatterns = [
    path('sellproduct/', sell_product_view, name="sellproduct"),
    path('store-products/', store_products_view, name="store-products"),
    path('store-products/detail/<int:product_id>', product_detail_view, name="product_detail"),    
    
]