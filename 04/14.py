def wystepuje(num,tab):
    suma=0
    for i in range (0,len(tab)):
        if int(tab[i])==num:
            suma+=1
    if suma>=1:
        print('Liczba wystepuje w tablicy')
    else:
        print('Liczba nie wystepuje w tablicy')           
tablica=[15,38,7,23,14]
liczba=23
print('Liczba: ',liczba)
print('Tablica:',end=' ')

for i in range (0,len(tablica)):
    if i==len(tablica)-1:
        print(tablica[i])
    else:
        print(tablica[i],end=' ')

print('Rezultat:',end=' ')
wystepuje(liczba,tablica)