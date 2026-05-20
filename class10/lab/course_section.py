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
    
    def __init__(self, title, capacity, enrolled):
        if (len(title) == 0):
            print("Course title cannot be empty")
        # elif (capacity < 0): #To ensure that error message prints if capacity cannot be created
        #     print("Course capacity must be greater than 0")
        else:
            self.title = title
            self.capacity = capacity
            self.enrolled = enrolled
    
    def display_info(self):
        print(f"CourseSection: title {self.title} - capacity {self.capacity} - enrolled {self.enrolled}")
    
    def register_student(self):
        new_enrolled = self.enrolled + 1
        if (new_enrolled > self.capacity):
            print("Failed to register student. This course is at capacity")
        else:
            self.enrolled += 1
    
    def drop_student(self):
        if (self.enrolled == 0):
            print("Failed to drop student. There are no students enrolled in this course")
        else:
            self.enrolled -= 1