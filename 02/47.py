ilosc = int(input('Podaj ilość pieniędzy: '))


dwa = (ilosc%5)//2
jeden = (dwa%2)
pięć = ilosc//5

if ilosc==1:
    print(f'Kwota {ilosc} w monetach: ')
    print(f'5 zł - 0 szt')
    print(f'2 zł - 0 szt')
    print(f'1 zł - 1 szt')
elif ilosc==2:
    print(f'Kwota {ilosc} w monetach: ')
    print(f'5 zł - 0 szt')
    print(f'2 zł - 1 szt')
    print(f'1 zł - 0 szt')
else:
    print(f'Kwota {ilosc} w monetach: ')
    print(f'5 zł - {pięć} szt')
    print(f'2 zł - {dwa} szt')
    print(f'1 zł - {jeden} szt')

print('Podaj kwote w zl: ')
x=int(input())
print(f'5zl: {x//5}')
print(f'2zl: {(x%5)//2}')
print(f'1zl: {((x%5)%2)//1}') 