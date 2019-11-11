x = int(input('Podaj liczbę dzieloną: '))
y = int(input('Podaj liczbę dzielącą: '))

if y==0 or x==0:
    print('Dzielenie przez zero!')
else:
    print(f'{x} / {y} = {x/y}') 