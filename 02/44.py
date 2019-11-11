limit=int(input('Podaj limit prędkości (w km/h): '))
predkosc=int(input('Podaj prędkość (w km/h): '))

if predkosc<limit:
    print('Brak mandatu')
elif predkosc>limit and predkosc-limit<=10:
    roznica = predkosc - limit
    mandat = roznica * 5
    print(f'Mandat wynosi: {mandat} zł')
elif predkosc>limit and predkosc-limit>10:
    roznica=predkosc-limit
    mandat=roznica*5
    mandat2=(roznica-10)*10
    mandat_final=mandat+mandat2
    print(f'Mandat wynosi: {mandat_final} zł') 