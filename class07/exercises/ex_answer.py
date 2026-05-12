# implement a basic notification system
from abc import ABC, abstractmethod

# 1. I want an interface / abstract class of Notification 
# abstractmethod --> send(self, message)
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass # do nothing for now
    
    @abstractmethod
    def receive(self, message):
        pass

    # concrete method    
    def describe(self):
        print("This is a notificaiton.") 

# 2. two concrete implementations of this class
# EmailNotification class
class EmailNotification(Notification):
    def __init__(self, email): # this is a constructor
        self.email = email

    def send(self, message): # this is an abstract method
        print(f"The message '{message}' was successfully sent to {self.email}")

    def receive(self, message): # this is an abstract method
        print(f"The message '{message}' was received.")
        
# SMSNotification class
class SMSNotification(Notification):
    def __init__(self, sms): # this is a constructor
        self.sms = sms

    def send(self, message): # this is an abstract method
        print(f"SMS: {message} was sent to {self.sms}")

    def receive(self, message): # this is an abstract method
        print(f"SMS: {message} was received.")

# 3. then use them here
def notify(notification, message):
    notification.send(message)

def receive_notification(notification, message):
    notification.receive(message)

email_user = EmailNotification("ABC@gmail.com")
sms_user = SMSNotification("123456789")

notify(email_user, "Hey")
notify(sms_user, "Hello")

receive_notification(email_user, "How are you?")
receive_notification(sms_user, "what's up?")

email_user.describe()