from student_record import StudentRecord
from course_section import CourseSection

student1 = StudentRecord("", 3.2, 12)
student2 = StudentRecord("Bob", -3.6, 62)
student3 = StudentRecord("Rob", 3.0, -22)

try:
    student = StudentRecord()
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
student4.update_gpa(1.0)
print()
student4.display_info()
student5.display_info()
print()
student4.display_info()
print(student4.academic_status)
student5.display_info()
print(student5.academic_status)
student6.display_info()
print(student6.academic_status)

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
print()
course9 = CourseSection("Digital Media Processsing", 10, 8, -2)
course9 = CourseSection("Digital Media Processsing", 10, 10, 0)
course9.display_info()
course9.register_student()
course9.display_info()
course9.add_to_waitlist()
course9.display_info()
course9.drop_student()
course9.display_info()
course9.remove_from_waitlist()
course9.display_info()

print()

def transferStudent (originalSection, transferSection):
    hasEnrolled = originalSection.enrolled > 0
    hasSpace = transferSection.enrolled < transferSection.capacity
    if (hasEnrolled and hasSpace):
        originalSection.drop_student()
        transferSection.register_student()
        print(f"Student was successfully transfered to {transferSection.title}")
    
    if (not hasEnrolled):
        print(f"Transfer failed.There are no students in {transferSection.title} section.")

    if (not hasSpace):
        print(f"Transfer failed.There is no space in {transferSection.title} section.")

transferStudent(course8, course7)
transferStudent(course9, course6)
transferStudent(course5, course8)
