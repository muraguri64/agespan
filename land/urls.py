from django.urls import path, include, re_path

from .views import lease_view, let_view, sell_view, buy_view, request_to_lease_view, all_let_lands_view, let_land_view, all_lease_requests_view, sell_land_view, all_buyer_requests_view, request_to_buy_view, all_sell_lands_view
                    

urlpatterns = [

    path('lease/', lease_view, name="lease"),
    path('view-to-lease/', all_let_lands_view, name="view-to-lease"),
    path('request-to-lease/', request_to_lease_view, name="request-to-lease"),

    path('let/', let_view, name="let"),
    path('let-land/', let_land_view, name="let-land"),
    path('view-lease-requests/', all_lease_requests_view, name="view-lease-requests"),

    path('sell/', sell_view, name="sell"),
    path('sell-land/', sell_land_view, name="sell-land"),
    path('view-buyer-requests/', all_buyer_requests_view, name="view-buyer-requests"),

    path('buy/', buy_view, name="buy"),
    path('view-to-buy/', all_sell_lands_view, name="view-to-buy"),
    path('request-to-buy/', request_to_buy_view, name="request-to-buy"),
    

    
]