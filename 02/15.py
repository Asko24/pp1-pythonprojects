x=int(input('Wprowadz dowolną liczbę od 1 do 10: '))

if x<1 or x>10:
    print('Podana liczba nie należy do przedziału od 1 do 10')
else:
    for i in range (1,11):
        print(f'{x} x {i} = {x*i}')