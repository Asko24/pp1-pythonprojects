tab=[15,8,31,47,2,19]
suma=0
ilosc=0
for i in range(0,len(tab)):
    if tab[i]%2==1:
        suma+=tab[i]
        ilosc+=1
    else:
        continue
print('Średnia liczb nie parzystych w tablicy: ',suma/ilosc)