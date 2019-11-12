tablica=[4,3,7,1,3]
def suma(x):
    suma=0
    for i in range (0,len(x)):
        suma+=x[i]
    return suma
print('Suma wartosci: ',suma(tablica))
    