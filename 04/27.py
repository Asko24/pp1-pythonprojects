string='Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'

a=0
e=0
i=0
o=0
y=0
u=0

for j in string:
    if j=='a':
        a+=1
    if j=='e':
        e+=1
    if j=='i':
        i+=1
    if j=='o':
        o+=1
    if j=='y':
        y+=1
    if j=='u':
        u+=1

print(f'Liczba liter\na: {a}\ne: {e}\ni: {i}\no: {o}\ny: {y}\nu: {u}')