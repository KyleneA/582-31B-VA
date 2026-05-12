from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def __init__(self, email_address):
        self.email_address = email_address

    def send(self, message):
        return f"To: {self.email_address}; {message}."

class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def send(self, message):
        return f"To: {self.phone_number}; {message}"

def send_notification(method, message):
    print(method.send(message))

email_notif = EmailNotification("example@email.com")
sms_notif = SMSNotification("514-123-4567")

send_notification(email_notif, "exercise is completed")
send_notification(sms_notif, "exercise is completed")