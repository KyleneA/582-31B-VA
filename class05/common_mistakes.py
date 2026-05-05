# Mistake 1: Forgetting cls in a class method
class Student: 
    school_name = "ABC"

    # this wouldn't work, because we miss the cls signature in our method
    @classmethod
    def show_school(): # HERE
        print(cls.school_name)


# Mistake 2 : using self in a class method
    # don't mix them up! 
    # BECAUSE --> class methods do not receive an instance
            # that's why we use cls, and not self

# Mistake 3: making something a static method when it needs class state
# for example:
@staticmethod
def change_school_name(new_name):
    cls.school_name = new_name

# ^^^^^ this doesn't pass!because we do not receive cls.

# Mistake 4: making something a class method when it is just a utility
# if a method only validates a string for example, it is probably better as a static method!

