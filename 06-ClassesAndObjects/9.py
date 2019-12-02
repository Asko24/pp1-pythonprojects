class University():
    
    def __init__ (self):
        self.name='UEK'
        self.fullname='Uniwersytet Ekonomiczny w Krakowie'
    
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name=new_name
    
    def print_fullname(self):
        print(self.fullname)
    
    def set_fullname(self, new_fullname):
        self.fullname=new_fullname
    


obiekt=University()
obiekt.print_name()
obiekt.print_fullname()
obiekt.set_name('AGH')
obiekt.set_fullname('Akademia Górniczo-Hutnicza w Krakowie')
obiekt.print_name()
obiekt.print_fullname()