from django.urls import path, include, re_path

from .views import market_view, market_detail_view


urlpatterns = [
    path('', market_view, name="market"), 
    path('<int:market_id>', market_detail_view, name="market_detail"), 
]