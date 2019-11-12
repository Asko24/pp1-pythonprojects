import re

komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)

suma=0
for i in range (0,len(cyfry)):
    suma+=int(cyfry[i])
    i+=1
print('Srednia temperatura: ',suma/len(cyfry))