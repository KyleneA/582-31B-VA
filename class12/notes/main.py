from review import ClassName

# Testing ClassName
object_instance1 = ClassName("attribute", "test")

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

print("----- INSTANCE METHOD -----")
#instance method
object_instance1.show_instance_attributes()

print("----- CLASS METHOD -----")
#class method
object_instance1.show_class_attributes()