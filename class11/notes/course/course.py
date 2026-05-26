from status import CourseStatus
from delivery import DeliveryMode

class Course:
    MAX_CAPACITY = 60

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, CourseStatus):
            raise ValueError("Status must be a CourseStatus value")
        else:
            self.__status = value
    
    @property
    def delivery_mode(self):
        return self.__delivery_mode
    
    @delivery_mode.setter
    def delivery_mode(self, value):
        if not isinstance(value, DeliveryMode):
            raise ValueError("Delivery mode must be a DeliveryMode value")
        else:
            self.__delivery_mode = value
    
    def __init__(self, title, capacity, status, delivery_mode):
        if capacity < 0 or capacity > self.MAX_CAPACITY:
            raise ValueError(f"Capacity must be greater or equal to 0 and smaller or equal to {MAX_CAPACITY}")
        else:
            self.title = title
            self.capacity = capacity
            self.status = status
            self.delivery_mode = delivery_mode
    
    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value} | Delivery mode: {self.delivery_mode.value}")

    def close_registration(self):
        if (self.is_open_for_registration() or self.status == CourseStatus.CANCELLED):
            self.status = CourseStatus.CLOSED
        else:
            raise ValueError("This course is already closed for registration.")
    
    def cancel_course(self):
        if (self.is_open_for_registration() or self.status == CourseStatus.CLOSED):
            self.status = CourseStatus.CANCELLED
        else:
            raise ValueError("This course has already been cancelled.")

    def reopen_course(self):
        if (self.status == CourseStatus.CANCELLED):
            self.status = CourseStatus.OPEN
        elif (self.status == CourseStatus.CLOSED):
            raise ValueError("This course has been cancelled.")
        else:
            raise ValueError("This course is already open for resgistration.")
    
    def is_open_for_registration(self):
        return self.status == CourseStatus.OPEN