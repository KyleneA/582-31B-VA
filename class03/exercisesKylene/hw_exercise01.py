# Playlist Class
class Playlist:
    def __init__(self, name, song_count):
        if (song_count >= 0):
            self.name = name
            self.song_count = song_count
            print(f"{self.name} playlist has been created")
        else:
            print("You cannot have a negative number for the song_count")
    
    def add_song(self):
        self.song_count += 1
        print(f"Song was added to {self.name} playlist")
    
    def remove_song(self):
        if (self.song_count > 0):
            self.song_count -= 1
            print(f"Song was removed from {self.name} playlist")
        else:
            print(f"Song was not removed. There aren't any songs in the {self.name} playlist.")
    
    def show_info(self):
        print(f"{self.name} playlist currently has {self.song_count} songs")

playlist1 = Playlist("calm songs", 25)
playlist2 = Playlist("workout songs", 15)
playlist3 = Playlist("commute songs", -1)
playlist3 = Playlist("commute songs", 0)

playlist3.remove_song()
playlist3.add_song()
playlist2.remove_song()
playlist1.show_info()

# ShoppingCart Class
class ShoppingCart:
    def __init__(self, owner, item_count):
        if (item_count >= 0):
            self.owner = owner
            self.item_count = item_count
            print(f"{self.owner}'s cart has been created")
        else:
            print("You cannot have a negative number for the item_count")

    def add_item(self):
        self.item_count += 1

    def remove_item(self):
        if (self.item_count > 0):
            self.item_count -= 1
            print(f"item was removed from {self.owner} cart")
        else:
            print(f"Item was not removed. There aren't any items in the {self.owner} cart.")
    
    def show_cart(self):
        print(f"{self.owner}'s cart currently has {self.item_count} items")

cart1 = ShoppingCart("Bob", 4)
cart2 = ShoppingCart("Rob", 0)
cart3 = ShoppingCart("Sol", -1)
cart3 = ShoppingCart("Sol", 8)

cart1.add_item()
cart2.remove_item()
cart3.remove_item()
cart2.show_cart()

# UserAccount Class
class UserAccount:
    def __init__(self, username, state = True, login_count = 0):
        if (login_count >= 0):
            self.username = username
            self.state = state
            self.login_count = login_count
            print(f"{self.username} account has been created")
        else:
            print("You cannot have a negative number for the login_count")
    
    def activate(self):
        if (self.state == False):
            self.state = True
        else:
            print(f"Activation failed. The {self.username} account is already active.")
    
    def deactivate(self):
        if (self.state == True):
            self.state = False
        else:
            print(f"Deactivation failed. The {self.username} account has already been deactivated.")
    
    def login(self):
        if self.state:
            self.login_count += 1
        else:
            print(f"Login failed. The {self.username} account is deactivated.")

    
    def show_status(self):
        if self.state:
            print(f"{self.username} account is active")
        else:
            print(f"{self.username} account is deactivated")

user1 = UserAccount("Joe")
user2 = UserAccount("Don", login_count = -1)
user2 = UserAccount("Don", login_count = 1)
user3 = UserAccount("Jol", state = False)

user1.activate()
user1.deactivate()
user3.deactivate()
user3.activate()
user2.login()
user1.login()
user3.show_status()
user1.show_status()