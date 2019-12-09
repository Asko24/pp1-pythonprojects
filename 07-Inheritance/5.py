class Utwory():
    
    def __init__(self, wykonawca, tytul, album, rok):
        self.wykonawca=wykonawca
        self.tytul=tytul
        self.album=album
        self.rok=rok
        
    def __str__(self):
        return f'Wykonawca: {self.wykonawca}\nUtwór: {self.tytul}\nAlbum: {self.album}\nRok: {self.rok}'
    
piosenka=Utwory('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', '2018')
print(piosenka)