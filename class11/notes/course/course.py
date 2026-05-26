from status import CourseStatus

class Course:
    def __init__(self, title, capacity, status):
        if not isinstance(status, CourseStatus):
            raise ValueError("Status must be a CourseStatus value")
        else:
            self.title = title
            self.capacity = capacity
            self.status = status
    
    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")

    def close_registration(self):
        if (self.status == CourseStatus.OPEN or self.status == CourseStatus.CANCELLED):
            self.status = CourseStatus.CLOSED
        else:
            raise ValueError("This course is already closed for registration.")
    
    def cancel_course(self):
        if (self.status == CourseStatus.OPEN or self.status == CourseStatus.CLOSED):
            self.status = CourseStatus.CANCELLED
        else:
            raise ValueError("This course has already been cancelled.")

    def reopen_course(self):
        if (self.status == CourseStatus.CANCELLED or self.status == CourseStatus.CLOSED):
            self.status = CourseStatus.OPEN
        else:
            raise ValueError("This course is already open for resgistration.")