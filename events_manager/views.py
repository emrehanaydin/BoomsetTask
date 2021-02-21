import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from events_manager.models import Events, Sessions, Speakers
from .serializers import EventsSerializer, SessionsSerializer, SpeakersSerializer
from rest_framework.decorators import action

logger = logging.getLogger(__name__)


class EventsAPIView(APIView):

    def get(self, request, event_id=None, *args, **kwargs):
        try:
            if event_id is None:
                events = Events.objects.filter()
                serializer = EventsSerializer(events, many=True)
            else:
                event = Events.objects.filter(id=event_id).first()
                serializer = EventsSerializer(event)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)

        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def pathc(self, request, *args, **kwargs):
        data = request.data

        event_id = data.pop("event_id")

        for key in data.keys():
            if key not in ["name", "start_date", "end_date", "is_active", "time_zone"]:
                data.pop(key)

        event = Events.objects.filter(id=event_id).update(data)

        serializer = self.get_serializer(event)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            "status": 200,
            "message": "Event Updated"
        })

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = EventsSerializer(
            data={
                "name": request.data.get("name"),
                "start_date": request.data.get("start_date"),
                "end_date": request.data.get("end_date")
            }
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "satus": 200,
                    "event_id": serializer.data["id"]
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionAPIView(APIView):
    def get(self, request, session_id=None, *args, **kwargs):
        try:

            if session_id is None:
                sessions = Sessions.objects.filter()
                serializer = SessionsSerializer(sessions, many=True)
            else:
                session = Sessions.objects.filter(id=session_id).first()
                print(session)
                serializer = SessionsSerializer(session)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)

        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def pathc(self, request, *args, **kwargs):
        data = request.data

        session_id = data.pop("session_id")

        for key in data.keys():
            if key not in ["name", "start_date", "event", "created_at", "end_date", "time_zone"]:
                data.pop(key)

        session = Sessions.objects.filter(id=session_id).update(data)

        serializer = self.get_serializer(session)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            "status": 200,
            "message": "Session Updated"
        })

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = SessionsSerializer(
            data={
                "name": request.data.get("name"),
                "event": request.data.get("event_id"),
                "start_date": request.data.get("start_date"),
                "end_date": request.data.get("end_date")

            }
        )

        if serializer.is_valid():
            serializer.save()

            return Response({"session_id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeakersAPIView(APIView):
    def get(self, request, speaker_id=None, *args, **kwargs):
        try:
            if speaker_id is None:
                spekaer = Speakers.objects.filter()
                serializer = SpeakersSerializer(spekaer, many=True)
            else:
                spekaers = Speakers.objects.filter(id=speaker_id).first()
                serializer = SpeakersSerializer(spekaers)

            return Response(
                {
                    "satus": 200,
                    "speaker": serializer.data
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            logger.error(e)

        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def pathc(self, request, *args, **kwargs):
        data = request.data

        speaker_id = data.pop("speaker_id")

        for key in data.keys():
            if key not in ["name", "start_date", "event", "created_at", "end_date", "time_zone"]:
                data.pop(key)

        speaker = Speakers.objects.filter(id=speaker_id).update(data)

        serializer = self.get_serializer(speaker)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            "status": 200,
            "message": "Speaker Updated"
        })

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = SpeakersSerializer(
            data={
                "first_name": request.data.get("first_name"),
                "last_name": request.data.get("last_name"),
                "session": request.data.get("session_id"),
                "start_date": request.data.get("start_date"),
                "end_date": request.data.get("end_date"),

            }
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "satus": 200,
                    "speaker_id": serializer.data["id"]
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
