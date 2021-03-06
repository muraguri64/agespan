from django.urls import path, include, re_path

from .views import post_event_view, upcoming_events_view, previous_events_view, event_detail_view


urlpatterns = [
    path('post-event/', post_event_view, name="post-event"),
    path('upcoming-events/', upcoming_events_view, name="upcoming-events"),
    path('previous-events/', previous_events_view, name="previous-events"),
    path('detail/<int:event_id>', event_detail_view, name="event_detail"),
    
 
]