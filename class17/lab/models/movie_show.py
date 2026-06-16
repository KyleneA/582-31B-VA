from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from core.exceptions import InvalidBookingError

class MovieShow:
    def __init__(self, title, capacity, status):
        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")