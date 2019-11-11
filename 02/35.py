a=float(input('Podaj współczynnik a: '))
b=float(input('Podaj współczynnik b: '))
c=float(input('Podaj wyraz wolny: '))

delta=b**2-4*a*c
print('delta: ',delta)
if delta>0:
    x1=(-1*b-delta**(1/2))/(2*a)
    x2=(-1*b+delta**(1/2))/(2*a)

    print('x1: ',x1)
    print('x2: ',x2)
elif delta==0:
    x1=(-1*b)/(2*a)
    print('x1: ',x1)
else:
    print('Delta ujemna. Brak rozwiązań w zbiorze liczb rzeczywistych.')