import logging

from events_manager.models import Events, Sessions, Speakers

logger = logging.getLogger(__name__)


class EventsWorker:
    @staticmethod
    def create_event(name: str, start_date: str, end_date: str) -> int:
        """ This function create event and returns event id"""
        try:
            event = Events(
                name=name,
                start_date=start_date,
                end_date=end_date
            )
            event.save()

            return event.id
        except Exception as e:
            logger.error(e)

        return 0

    @staticmethod
    def get_event(event_id:int):
        try:
            event = Events(
                name=name,
                start_date=start_date,
                end_date=end_date
            )
            event.save()

            return event.id
        except Exception as e:
            logger.error(e)

        return 0