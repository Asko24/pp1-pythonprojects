i=1
tab=[]
count=0

while i>0:
    y=int(input('Podaj liczbę: '))
    if y==0:
        break
    else:
        tab.append(y)
        count+=1

print(f'REZULTAT: Liczb={count}, Suma={sum(tab)}, Średnia={(sum(tab))/count}')