class Message():
    def __init__(self):
        self.message = ''
    def set_message(self, message):
        count = 0
        for i in message:
            count += 1
            if count == 1:
                self.message += i.upper()
            else:
                self.message += i.lower()


class SMS():
    def __init__(self, number1, number2):
        self.number_of_sender = number1
        self.number_of_recipient = number2



a = Message()
a.set_message("Hej")