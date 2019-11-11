pesel=input('Podaj PESEL: ')
cyfry_wieku=int(pesel[0:2])
cyfry_miesiaca=int(pesel[2:4])

if int(pesel[9])%2==0:
    płeć='kobieta'
else:
    płeć='mężczyzna'
    
print('Płeć: ',płeć)
if cyfry_miesiaca>12:
    print('Wiek: ',cyfry_wieku)
else:
    print('Wiek: ',2018-(1900+cyfry_wieku))
