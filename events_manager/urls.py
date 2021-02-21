from django.conf.urls import url
from django.urls import path, include
from events_manager.views import EventsAPIView, SessionAPIView, SpeakersAPIView

urlpatterns = [
    path('create/event', EventsAPIView.as_view()),
    path('update/event', EventsAPIView.as_view()),
    path('list/events', EventsAPIView.as_view(), name="list-events"),
    path('get/event/<event_id>', EventsAPIView.as_view(), name="get-event"),

    path('create/session', SessionAPIView.as_view()),
    path('update/session', SessionAPIView.as_view()),
    path('list/sessions', SessionAPIView.as_view(), name="list-sessions"),
    path('get/session/<session_id>', SessionAPIView.as_view(), name="get-session"),

    path('create/speaker', SpeakersAPIView.as_view()),
    path('update/speaker', SpeakersAPIView.as_view()),
    path('list/speakers', SpeakersAPIView.as_view(), name="list-spekars"),
    path('get/speaker/<speaker_id>', SpeakersAPIView.as_view(), name="get-spekar"),

]
