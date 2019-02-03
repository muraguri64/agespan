from django.urls import path, include, re_path

from .views import request_to_lease_view, all_let_lands_view


urlpatterns = [
    path('view-to-lease/', all_let_lands_view, name="view-to-lease"),
    path('request-to-lease/', request_to_lease_view, name="request-to-lease"),

    
]