from rest_framework import serializers
from events_manager.models import Events, Sessions, Speakers


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ["id", "name", "start_date", "end_date", "time_zone", "created_at", "is_active"]


class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = ["id", "name", "start_date", "event", "end_date", "created_at", "is_active"]

class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ["id", "first_name", "last_name", "session", "start_date", "end_date", "is_active"]
