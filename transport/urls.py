from django.urls import path, include, re_path

from .views import request_transport_view, offer_transport_view, all_transport_requests_view, transport_request_detail_view, all_transport_offers_view, transport_offer_detail_view


urlpatterns = [
    path('request-transport/', request_transport_view, name="request-transport"),
    path('all-transport-requests/', all_transport_requests_view, name="all-transport-requests"),
    path('offer-transport/', offer_transport_view, name="offer-transport"),
    path('all-transport-offers/', all_transport_offers_view, name="all-transport-offers"),
   
    #Details url
    path('transport-request/detail/<int:request_id>', transport_request_detail_view, name="transport_request_detail"),
    path('transport-offer/detail/<int:offer_id>', transport_offer_detail_view, name="transport_offer_detail"),
]