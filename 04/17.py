import random

tab=[]

def rzucKostka(ilosc):
    for i in range (0,ilosc):
        x=random.randrange(1,6)
        tab.append(x)

ilosc_rzutow=int(input('Ile razy rzucamy kostka?: '))
rzucKostka(ilosc_rzutow)

        
print('Wyrzucone oczka: ',end='')
    
for i in range (0,len(tab)):
    print(tab[i],end=' ')
    
print('\nSuma oczek:',end=' ')
    
suma=0
    
for j in range (0,len(tab)):
    suma+=tab[j]
print(suma)
    