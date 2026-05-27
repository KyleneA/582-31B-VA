from abc import ABC, abstractmethod

class AbstractMethod(ABC):
    @abstractmethod
    def print_attribute(self):
        pass

class ClassName(AbstractMethod):
    # CONSTANT
    CONSTANT_NAME_STRING = "never changes"
    CONSTANT_NAME_NUMBER = 25

    # STATIC METHOD
    @staticmethod
    def is_valid_value(value):
        return len(value) > 0

    # CLASS ATTRIBUTES
    class_attribute_string = "something"
    class_attribute_number = 50

    # CLASS METHOD
    @classmethod
    def show_class_attributes(cls):
        print(f"Class string: {cls.class_attribute_string} | Class number: {cls.class_attribute_number}")
        print()
    
    # CONSTRUCTOR
    def __init__(self, attribute, property_name):
        self.instance_attribute = attribute
        self.property_name = property_name
        self.show_instance_attributes()

    # ALTERNATIVE CONSTRUCTOR
    @classmethod
    def from_string(cls, string):
        attribute, property_name = string.strip().split(",") # removing spaces & splitting into different variables
        return cls(attribute, property_name)
    
    @classmethod
    def from_dict(cls, dict):
        attribute = dict["attribute"]
        property_name = dict["property_name"]
        return cls(attribute, property_name)

    # PROPERTIES
    @property 
    def property_name(self):
        return self.__property_name # private property

    @property_name.setter
    def property_name(self, value):
        condition = ClassName.is_valid_value(value) # calling needs class name for static method
        if condition:
            self.__property_name = value
        else:
            raise ValueError("The value given doesn't fill the required condition")
    
    # INSTANCE METHODS
    def show_instance_attributes(self):
        print(f"Instance attribute: {self.instance_attribute} | Property name: {self.property_name}")
        print()
    
    # ABSTRACT METHOD
    def print_attribute(self):
        print("This abstract method makes sure that all classes with the type AbstractMethod have a method called 'print_attribute'.")
        print(f"Attribute: {self.instance_attribute}")
        print()


