import random
x=random.randint(-100,100)
y=random.randint(-100,100)

print('Piersza liczba: ',x)
print('Druga liczba: ',y)
if x<y:
    print('Większą liczbą jest: ',y)
elif x==y:
    print('Liczby są równe')
else:
    print('Większą liczbą jest: ',x)