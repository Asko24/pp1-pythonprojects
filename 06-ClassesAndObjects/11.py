class TV():
    
    def __init__(self):
        self.is_on=0
        self.channel_no=1
        
    def on(self):
        self.is_on=1
    
    def off(self):
        self.is_on=0
        
    def show_status(self):
        if self.is_on==1:
            print('Telewizor jest włączony',end=', ')
        else:
            print('Telewizor jest wyłączony',end=', ')
        print(f'kanał {self.channel_no}')
    
    def set_channel(self, new_channel_no):
        self.channel_no=new_channel_no
        
        

telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.off()
telewizor.show_status()
telewizor.set_channel(5)
telewizor.show_status()