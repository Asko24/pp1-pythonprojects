class TV():
    
    def __init__(self):
        self.is_on=0
        self.channels=[]
        
    def on(self):
        self.is_on=1
    
    def off(self):
        self.is_on=0
        
    def show_status(self):
        if self.is_on==1:
            print('Telewizor jest włączony',end=', ')
        else:
            print('Telewizor jest wyłączony',end=', ')
        if len(self.channels)==0:
            print('brak kanałów')
        else:
            print(f'kanał {self.channel_no}')
    
    def set_channels(self, channels_list):
        self.channels=channels_list
        
    def show_channels(self):
        if len(self.channels)==0:
            print('Lista kanalow jest pusta')
        else:
            print('LISTA KANALOW TV')
            for i in range (0,len(self.channels)):
                print(self.channels[i])
        
        
        

telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.off()
telewizor.show_status()
telewizor.show_channels()
telewizor.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox'])
telewizor.show_channels()
telewizor.show_status()
