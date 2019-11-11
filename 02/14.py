wiek=float(input('Podaj wiek psa w ludzkich latach: '))

if wiek<2:
    print(f'Wiek psa w psich latach to {wiek*10.5} lata')
else:
    print(f'Wiek psa w psich latach to {(wiek-2)*4+21}')