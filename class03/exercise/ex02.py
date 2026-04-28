# create a class User
class User:
    # give two attributes (username, password)
    def __init__(self, username, password):
        # Option A:
        if(len(password) < 4):
            print("password is too short")
        else:
            self.username = username
            self.password = password
        
        # Option B:
        #self.username = username
        #self.password = self.set_password(password)
    
    # both in password setter function and __init__:    
        # if password is less than 4 characters long, return an error! (can be just a print statement)
    def set_password(self, new_password):
        if(len(new_password) < 4):
            print("invalid password, it must contain at least 4 characters")
        else:
            self.password = new_password
            

# user1 = User("abc", "12345")
user2 = User("def", "123")
print(user2.username)