from message import Message

class SMS(Message):
    
    def __init__(self, numernadawcy, numerodbiorcy, temat):
        self.numernadawcy=numernadawcy
        self.numerodbiorcy=numerodbiorcy
        self.temat=temat
        
    def send(self):
        wiadomosc=Message.self.message
        
        print("Wysyłanie SMS'a...")
        print(f'OD: {self.numernadawcy}')
        print(f'DO: {self.numerodbiorcy}')
        print(f'TEMAT: {self.temat}')
        print(f'WIADOMOSC: {wiadomosc}')

        
sms=SMS(112,997,'Hej')
sms.send()