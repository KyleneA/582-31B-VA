## Constant vs Enum
### Constant
Definition: Value that should not change during the program
> [!Syntax]
> UPPERCASE
>> `MAX_STUDENTS = 30`
>> `DEFAULT_CREDITS = 3`
>> `STATUS_OPEN = "open"`
#### Why constants
- for use of 
	- one fixed number
	- one repeated string
	- configuration values

### Enum
> [!Definition] 
> Special *type* used to define a fixed set of **named** values

```python
from enum import Enum # Importing the class

# can choose from one of the following
class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled" 
```

> [!important]
> 1. enum members are not plain strings
> 2. to compare, must compare with **enum members not random strings**
> 	- it will still work with a regular string, but its convention to compare with enum members when possible
> 3. can require that a variable be a valid enum member when making a class.
> 	- example: 
> ```python
> 		 if not isinstance(status, CourseStatus):
 >           raise ValueError("Status must be a CourseStatus value")
> ```
#### Why use enums
- Make allowed values more explicit
- improve readability
- reduce typos/spelling mistakes
- makes validation easier
- improves program design

#### Examples
```python
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
```
```python
# looping though possible options
from enum import Enum

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

for priority in Priority:
    print(priority, priority.value)
```
