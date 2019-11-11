liczba=list(input('Podaj liczbę: '))
nazwy=['zero ', 'jeden ', 'dwa ', 'trzy ', 'cztery ', 'pięć ', 'sześć ', 'siedem ', 'osiem ', 'dziewięć ']

for i in liczba:
    i = int(i)
    print(nazwy[i], end = ' ')