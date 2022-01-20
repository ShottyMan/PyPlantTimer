import json
import datetime


class Scheduler:
    def __init__(self):
        """Inits the class by creating or reading from a json file."""
        self.current_time = datetime.datetime.now()
        self.name = 1
        self.event_dict = {}

    def check_time(self, event_time: tuple):
        """compares the current time and the trigger date of the event

        Args:
            event_time (tuple): (weekday (0-6) hour (0-24), minute(0-60))

        Returns:
            Bool: True if match, false if don't match.
        """
        return (
            self.current_time.weekday,
            self.current_time.hour,
            self.current_time.minute,
        ) == event_time

    def update_time(self):
        """Update the class's current time."""
        self.current_time = datetime.datetime.now()

    def new_event(self, day: int, hour: int, minute: int):
        """Add a new event to the event dictionary.

        Args:
            day (int): Day, 0-6, Monday through Friday
            hour (int): Hour, 0-24
            minute (int): Minute, 0-59
        """
        self.event_dict.update({self.name: (day, hour, minute)})
        self.name += 1

    def load_json(self, json):
        try:
            self.event_dict = json.load(open("events.json", "w", encoding="utf-8"))
        except OSError:
            print(
                "Weird. An OS error occured. This really shouldn't happen. Sorry, but we're shutting down."
            )
            raise OSError from OSError
        except json.JSONDecodeError:  # if the file is empty, initialize the event dict
            self.event_dict = {}