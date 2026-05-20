from student_record import StudentRecord
from course_section import CourseSection

student1 = StudentRecord("", 3.2, 12)
student2 = StudentRecord("Bob", -3.6, 62)
student3 = StudentRecord("Rob", 3.0, -22)

try:
    student4 = StudentRecord()
except TypeError as e:
    print("Error:", e)

print()
student4 = StudentRecord("Don", 3.2, 12)
student5 = StudentRecord("Bob", 3.6, 62)
student6 = StudentRecord("Rob", 3.0, 22)
student4.display_info()
student5.display_info()
student6.display_info()
print()
student4.add_credits(-8)
student5.add_credits(8)
student6.update_gpa(-8)
student6.update_gpa(8)
student2.update_gpa(4.0)
print()
student4.display_info()
student5.display_info()

print()
print("==========")
print()

course1 = CourseSection("", 20, 10)
try:
    course2 = CourseSection("Adv. web programming", -20, 10)
except AttributeError as e:
    print("Error:", e)
try:
    course2 = CourseSection("Adv. web programming", 0, 10)
except AttributeError as e:
    print("Error:", e)
course3 = CourseSection("Web interface programming", 20, -10)
course4 = CourseSection("Applied UX UI", 20, 30)

try:
    course = CourseSection()
except TypeError as e:
    print("Error:", e)

print()
course5 = CourseSection("Intro to CMS", 20, 17)
course6 = CourseSection("Adv. web programming", 30, 30)
course7 = CourseSection("Web interface programming", 20, 16)
course8 = CourseSection("Applied UX UI", 20, 0)
course5.display_info()
course6.display_info()
course7.display_info()
course8.display_info()
print()
course5.register_student()
course6.register_student()
course7.drop_student()
course8.drop_student()
print()
course5.display_info()
course6.display_info()
course7.display_info()
course8.display_info()