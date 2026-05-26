from course import Course
from status import CourseStatus

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED)
course3 = Course("Digital Media Processing", 25, CourseStatus.CANCELLED)

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