a=int(input('Podaj pierwszą liczbę: '))
b=int(input('Podaj drugą liczbę: '))
c=int(input('Podaj trzecią liczbę: '))

if a>=b and a<=c:
    print(f'Liczby w kolejności rosnącej: {b}, {a}, {c}')
elif a>=c and a<=b:
    print(f'Liczby w kolejności rosnącej: {c}, {a}, {b}')
elif b>=a and b<=c:
    print(f'Liczby w kolejności rosnącej: {a}, {b}, {c}')
elif b>=c and b<=a:
    print(f'Liczby w kolejności rosnącej: {c}, {b}, {a}')
elif c>=a and c<=b:
    print(f'Liczby w kolejności rosnącej: {a}, {c}, {b}')
elif c>=b and c<=a:
    print(f'Liczby w kolejności rosnącej: {b}, {c}, {a}')