class TV():
    
    def __init__(self):
        self.is_on=0
        
    def on(self):
        self.is_on=1
    
    def off(self):
        self.is_on=0
        
    def show_status(self):
        if self.is_on==1:
            print('Telewizor jest włączony')
        else:
            print('Telewizor jest wyłączony')

telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.off()
telewizor.show_status()