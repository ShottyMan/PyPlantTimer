import json
import datetime


class Scheduler:
    def __init__(self):
        """Inits the class."""
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

    def load_json(self, json_file):
        """Fill the local dictionary with the contents of a json file.

        Args:
            json_file (json): The json file that will be loaded.

        Raises:
            OSError: If there is an error loading the file
        """
        try:
            self.event_dict = json.load(json_file)
        except json.JSONDecodeError:
            print("The json couldn't be loaded. This is fatal.")
            raise ValueError from ValueError
