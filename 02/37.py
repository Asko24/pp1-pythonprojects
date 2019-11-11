a=float(input('Podaj pierwszą liczbę: '))
b=float(input('Podaj drugą liczbę: '))
c=float(input('Podaj trzecią liczbę: '))

if a>b and a<c:
    print(f'Mediana: {a}')
elif a>c and a<b:
    print(f'Mediana: {a}')
elif b>a and b<c:
    print(f'Mediana: {b}')
elif b>c and b<a:
    print(f'Mediana: {b}')
elif c>b and c<a:
    print(f'Mediana: {c}')
elif c>a and c<b:
    print(f'Mediana: {c}')
elif a==b or b==a:
    print(f'Mediana: {(a+b)/2}')
elif b==c or c==b:
    print(f'Mediana: {(c+b)/2}')
elif a==c or c==a:
    print(f'Mediana: {(c+a)/2}')