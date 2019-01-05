from django.urls import path, include, re_path

from .views import request_transport_view, offer_tranport_view, all_transport_requests_view, all_transport_offers_view


urlpatterns = [
    path('request-transport/', request_transport_view, name="request-transport"),
    path('all-transport-requests/', all_transport_requests_view, name="all-transport-requests"),
    path('offer-transport/', offer_tranport_view, name="offer-transport"),
    path('all-transport-offers/', all_transport_offers_view, name="all-transport-offers"),
    
]