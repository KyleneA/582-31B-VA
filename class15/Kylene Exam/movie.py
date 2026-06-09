from theater import TheaterRoom, ScreaningTime, ShowStatus
from helperMethods import HelperMethods
from customExceptions import InvalidBookingError, ShowSoldOutError, ShowCancelledError, InvalidStatusError

class MovieShow:
    MAX_TICKETS_PER_BOOKING = 10

    def __init__(self, title, capacity, booked_seats = 0, status = ShowStatus.OPEN):
        if not HelperMethods.is_valid_input(title, 0):
            raise ValueError("Movie title must contain at least 1 letter")
        else:
            self.__title = title
            self.capacity = capacity
            self.booked_seats = booked_seats
            self.status = status
    
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be a positive number greater than 0")
        else:
            self.__capacity = value
    
    @property
    def booked_seats(self):
        return self.__booked_seats
    
    @booked_seats.setter
    def booked_seats(self, value):
        if value < 0:
            raise ValueError("Number of booked seats must be a positive number")
        elif value > self.__capacity:
            raise ValueError("Number of booked seats cannot exceed capacity")
        else:
            self.__booked_seats = value
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, ShowStatus):
            raise InvalidStatusError("Status must be a member of ShowStatus")
        ## REMOVED BELOW BECAUSE IT CONFLICTS WITH BONUS A
        # elif self.is_full() and value == ShowStatus.OPEN:
        #     raise InvalidStatusError("Status cannot be open if booked seats is at capacity")
        else:
            self.__status = value

    def remaining_seats(self):
        return self.capacity - self.booked_seats

    def is_full(self):
        if self.remaining_seats() == 0:
            return True
        else:
            return False

    def display_info(self):
        return f"Title: {self.__title} | Capacity: {self.capacity} | Status: {self.status.value} | Booked seats: {self.booked_seats}, Remaining seats: {self.remaining_seats()}"

    def book_tickets(self, customer, quantity):
        if self.status == ShowStatus.SOLD_OUT:
            raise ShowSoldOutError("Booking is closed because the showing is sold out")
        elif quantity < 0:
            raise InvalidBookingError("Quantity must be greater than 0")
        elif quantity > MovieShow.MAX_TICKETS_PER_BOOKING:
            raise InvalidBookingError(f"You cannot book more than {MovieShow.MAX_TICKETS_PER_BOOKING} per session")
        elif self.booked_seats + quantity > self.capacity:
            raise InvalidBookingError(f"You cannot book {quantity} tickets. There are only {self.remaining_seats()} seats available.")
        elif self.status == ShowStatus.CANCELLED:
            raise ShowCancelledError("Booking is closed because the showing has been cancelled")
        else:
            self.booked_seats += quantity
            if self.booked_seats == self.capacity:
                self.status = ShowStatus.SOLD_OUT
    
    def cancel_show(self):
        if self.status == ShowStatus.OPEN or self.status == ShowStatus.SOLD_OUT:
            self.status = ShowStatus.CANCELLED
        else:
            raise InvalidStatusError("The MovieShow status is already set to cancelled")
    
    def reopen_show(self):
        if self.status == ShowStatus.SOLD_OUT:
            self.status = ShowStatus.OPEN
        elif self.status == ShowStatus.CANCELLED:
            raise InvalidStatusError("Cancelled shows cannot be reopenned")
        else:
            raise InvalidStatusError("The MovieShow status is already set to open")
