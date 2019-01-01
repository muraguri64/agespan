from django.urls import path, include, re_path

from .views import register_agronomist_view, all_agronomists_view, request_agronomist_view, all_requested_agronomists_view


urlpatterns = [
    path('register-agronomist/', register_agronomist_view, name="register-agronomist"),
    path('all-agronomists/', all_agronomists_view, name="all-agronomists"),
    path('request-agronomist/', request_agronomist_view, name="request-agronomist"),
    path('all-requested-agronomists/', all_requested_agronomists_view, name="all-requested-agronomists"),
    



    
    
]