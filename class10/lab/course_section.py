class CourseSection:
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if (value <= 0):
            print("Course capacity must be greater than 0")

        else:
            self.__capacity = value
    
    @property
    def enrolled(self):
        return self.__enrolled
    
    @enrolled.setter
    def enrolled(self, value):
        if ((0.0 > value) or (value > self.capacity)):
            print("The number of students enrolled must be greater or equal to 0 AND smaller or equal to capacity")
        else:
            self.__enrolled = value
    
    @property
    def waitlist(self):
        return self.__waitlist
    
    @waitlist.setter
    def waitlist(self, value):
        if (value < 0):
            print("Waitlist cannot be a negative number")
        else:
            self.__waitlist = value
    
    def __init__(self, title, capacity, enrolled, waitlist = 0):
        if (len(title) == 0):
            print("Course title cannot be empty")
        # elif (capacity < 0): #To ensure that error message prints if capacity cannot be created
        #     print("Course capacity must be greater than 0")
        else:
            self.title = title
            self.capacity = capacity
            self.enrolled = enrolled
            self.waitlist = waitlist
    
    def display_info(self):
        print(f"CourseSection: title {self.title} - capacity {self.capacity} - enrolled {self.enrolled} - waitlist {self.waitlist}")
    
    def register_student(self):
        new_enrolled = self.enrolled + 1
        if (new_enrolled > self.capacity):
            print("Failed to register student. This course is at capacity. Student was added to waitlist")
            self.add_to_waitlist()
        else:
            self.enrolled += 1
    
    def drop_student(self):
        if (self.enrolled == 0):
            print("Failed to drop student. There are no students enrolled in this course")
        else:
            self.enrolled -= 1
            if (self.waitlist > 0):
                print(f"Student from waitlist was added to {self.title}")
                self.register_student()
                self.remove_from_waitlist()
    
    def add_to_waitlist(self):
        self.waitlist += 1
    
    def remove_from_waitlist(self):
        if (self.waitlist == 0):
            print("Failed to remove from waitlist. Waitlist is empty")
        else:
            self.waitlist -= 1