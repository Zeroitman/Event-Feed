from django.urls import path
from event_feed.views import EventFeedAPIView

app_name = "event_feed"

urlpatterns = [
    path("event-feed/<int:pk>/", EventFeedAPIView.as_view())
]