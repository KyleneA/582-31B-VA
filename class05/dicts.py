# what is a dictionary?

# a dictionary maps a value to a key !

# examples of dictionaries:
# in a phone book --> a phone number is associated to a name
# in a word dictionary --> a definition is associated to a word

# in programming:
# a dictionary is ALWAYS --> a value associated to a key

# FORMULA:
# VARIABLE = {KEY:VALUE, KEY2:VALUE, etc..}

my_dict = {"name": "Jane", "program": "Computer Science", "semester": 3}
print(my_dict)
print(my_dict["name"]) # the value that is associated to the key
print(my_dict["program"])
print(my_dict["semester"])

my_dict["semester"] = 30
print(my_dict["semester"])