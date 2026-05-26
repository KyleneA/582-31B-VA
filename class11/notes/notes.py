from enum import Enum

class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

status = CourseStatus.OPEN
print(status)
print(status.value)

if status == CourseStatus.OPEN:
    print("Registration is allowed.")

# --------------

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

for priority in Priority:
    print(priority, priority.value)

# --------------
print()
if status.value == "open":
    print("Open")