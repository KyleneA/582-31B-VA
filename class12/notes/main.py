from review import ClassName, EnumClass
from abstractMethod import Shape, Rectangle, Circle

# Testing ClassName
object_instance1 = ClassName("attribute", "test", EnumClass.ATTRIBUTE1)
object_instance7 = ClassName("attribute", "test", EnumClass.ATTRIBUTE3)

# alternative constructor
object_instance3 = ClassName.from_string("AtTrIbUtE, test")

example_dict = {
    # keys have to be in ""
    "attribute": "AttributE", 
    "property_name": "Test"
}
object_instance5 = ClassName.from_dict(example_dict)

#invalid inputs
try:
    object_instance2 = ClassName("Attribute", "")
except ValueError as e:
    print("Error: ", e)
    print()

try:
    object_instance4 = ClassName.from_string("AttriBute,")
except ValueError as e:
    print("Error: ", e)
    print()

try:
    bad_dict = {
        "attribute": "AttrIBute",
        "property_name": ""
    }

    object_instance6 = ClassName.from_dict(bad_dict)
except ValueError as e:
    print("Error: ", e)
    print()

try:
    object_instance8 = ClassName("attribute", "test", "option2")
except ValueError as e:
    print("Error: ", e)
    print()

print("----- PROPERTIES -----")
# stored & managed property
print("Stored & managed property (property_name): ", object_instance1.property_name)
print("Computed property (attribute_length): ", object_instance1.attribute_length)
print()

print("----- INSTANCE METHOD -----")
#instance method
object_instance1.show_instance_attributes()

print("----- CLASS METHOD -----")
#class method
object_instance1.show_class_attributes()

print("----- ABSTRACT METHOD -----")
#abstract method
rectangle = Rectangle(2, 4)
circle = Circle(3)

print(f"Lecture Example: rectangle area is: {rectangle.area()}; circle area is: {circle.area()}")
print()

object_instance1.print_attribute()
