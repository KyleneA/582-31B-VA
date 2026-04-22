# Going through basics
print("hello world")

num1 = 5
num2 = 10

print(num1 + num2)

# function
def my_function(num1, num2):
    return num1 + num2
# indentation indicates what is part of the function

# conditionals
if (num1 < num2):
    print(my_function(num1, num2))
    print("true")
else:
    print("false")

a = 4
if ((a > 3 and a < 6) or a == 4):
    print("Hey")

# classes
class MyClass():
    x = 5

myClass1 = MyClass()

print(myClass1.x)

# user input 
# user_name = input("what is your name?")
# print("welcome", user_name)

# for loops
for i in range(0, 5):
    print(i)

# lists
my_list = [1, 3, 5, 7]
mixed_list = [1, True, "hello", 10.5]

print(my_list)

# for each loop 
for i in my_list:
    print(i)


# break and continue
for i in range (0, 6):
    if (i == 3):
        continue # ignores commands after and goes to thhe next i
    if (i == 5):
        break # ignores commands after and exits the loop
    print(i)

# while loop
a = 5
while (a > 0):
    print("while!", a)
    a-=1