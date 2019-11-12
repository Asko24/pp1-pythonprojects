tablica=[4,3,7,1,3]
def suma(x):
    suma=0
    for i in range (0,len(x)):
        suma+=x[i]
    return suma

def tablica_print(y):
    for i in range (0,len(y)):
        print(y[i],end=' ')


print('Tablica: ',tablica_print(tablica))
print('Suma wartosci: ',suma(tablica))
    