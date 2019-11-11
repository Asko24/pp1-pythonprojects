n = int(input('Podaj liczbę: '))

tab=[]
tab2=[]

while n > 0:
    x = n%2
    tab2.append(x)
    tab.insert(0,x)
    n=n//2

print(tab)
print(tab2)