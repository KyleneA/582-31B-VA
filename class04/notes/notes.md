## Class attributes
> [!comparison]
> instance attribute -> 
>> created with self, 
>> usually defined in def __init, 
>> different per object
 >
 > class attribute -> 
>>defined in class body, 
>> shared across all instances

Best used when the attribute is:
- shared across all instances
- conceptually the same for all instances
- usually configuration-like or constant-like
- they're counters or class-wide metadate

```python
class Employee:
    base_salary = 500
    bonus = 0.25
    company_name = "582-31B"
    
    def __init__(self):
	    self.name = name
        self.sales_count = sales_count
        print(f"Employee {self.name} has been created")
```
### Class methods with class attributes
#### Ways to call a class attribute in a class method
**Using self**
- `self.base_salary`
- more recommended to use
**Using class name**
- `Employee.base_salary`
- can be used to change attribute for all instances of the class

### Shadowing a Class attribute
> [!definition]
> shadow attribute is an instance attribute of a class attribute (different for 1 or more instances of the Class object from the rest of the instances of the class) 
> 
>> ex from code below: e3 has a shadow attribute for bonus

```python
e1 = Employee("Bob", 9)
e2 = Employee("Rob", 10)
e3 = Employee("Ron", 11)

print(f"{e1.name}'s bonus is {e1.bonus}") # -> Bob's bonus is 0.25
print(f"{e2.name}'s bonus is {e2.bonus}") # -> Rob's bonus is 0.25
print(f"{e3.name}'s bonus is {e3.bonus}") # -> Ron's bonus is 0.25

Employee.bonus = 1

print(f"{e1.name}'s bonus is {e1.bonus}") # -> Bob's bonus is 1
print(f"{e2.name}'s bonus is {e2.bonus}") # -> Rob's bonus is 1
print(f"{e3.name}'s bonus is {e3.bonus}") # -> Ron's bonus is 1

e3.bonus = 2 

print(f"{e1.name}'s bonus is {e1.bonus}") # -> Bob's bonus is 1
print(f"{e2.name}'s bonus is {e2.bonus}") # -> Rob's bonus is 1
print(f"{e3.name}'s bonus is {e3.bonus}") # -> Ron's bonus is 2

e4 = Employee("Von", 5)

print(f"{e1.name}'s bonus is {e1.bonus}") # -> Bob's bonus is 1
print(f"{e2.name}'s bonus is {e2.bonus}") # -> Rob's bonus is 1
print(f"{e3.name}'s bonus is {e3.bonus}") # -> Ron's bonus is 2
print(f"{e4.name}'s bonus is {e4.bonus}") # -> Von's bonus is 1

```