class University():
    
    def __init__ (self):
        self.name='UEK'
    
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name=new_name
    


obiekt=University()
obiekt.print_name()
obiekt.set_name('AGH')
obiekt.print_name()