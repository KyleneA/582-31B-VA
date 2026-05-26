from course import Course
from status import CourseStatus
from delivery import DeliveryMode
from student import Student
from studentLevel import StudentLevel

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN, DeliveryMode.ONLINE)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED, DeliveryMode.IN_PERSON)
course3 = Course("Digital Media Processing", 25, CourseStatus.CANCELLED, DeliveryMode.HYBRID)

try:
    course1.display_info()
    course2.display_info()
    course3.display_info()

    course1.close_registration()
    course1.display_info()

    course2.reopen_course()
    course2.display_info()
except ValueError as e:
    print("Error:", e)

try:
    course1.close_registration()
    course1.display_info()
except ValueError as e:
    print("Error:", e)

try:
    course2.reopen_course()
    course2.display_info()
except ValueError as e:
    print("Error:", e)

try:
    course3.cancel_course()
    course3.display_info()
except ValueError as e:
    print("Error:", e)

# REFLECTION
# What is the difference between a constant and an enum?
## Constant is a single variable that doesn't change that can be a string or number
## Enum class is a set number of string options that can be used to ensure that there are less errors in the code and that it is more readable.

# Why are enums safer than random strings?
## Enums help ensure there are no typos and can make the code easier to read

# Why is CourseStatus.OPEN better than "open"?
## This ensures that the options for status fall within the options set within the CourseStatus Enum class

# Why did you use a property for status?
## Using the property makes it harder to change the value of status to any value that doesn't comply with the conditions set within it's setter.

# How do enums help validation in class design?
## It helps ensure that the value you are setting for the property or attribute is written exactly how you entend it to.

print()

student1 = Student("bob", StudentLevel.BEGINNER)
student2 = Student("rob", StudentLevel.INTERMEDIATE)
student3 = Student("ron", StudentLevel.ADVANCED)

student1.display_info()
student2.display_info()
student3.display_info()