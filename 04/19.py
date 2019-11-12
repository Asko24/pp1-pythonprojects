def suma(n):
    if n==0:
        print('Podana liczba jest mniejsza od 1')
    
    if n==1:
        return 1
    
    if n>1:
        return n+suma(n-1)
    
print(f'Suma przedziału <1,500> : {suma(500)}')


#sprawdzenie
suma=0
for i in range (1,501):
    suma+=i
print(suma)