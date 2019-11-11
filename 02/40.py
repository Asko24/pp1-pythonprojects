import random
tab = []
for i in range(1,101):
    j = random.randrange(1,7)
    tab.append(j)
    x1=tab.count(1)
    x2=tab.count(2)
    x3=tab.count(3)
    x4=tab.count(4)
    x5=tab.count(5)
    x6=tab.count(6)
print(f'Jedynek wypadło: {x1}')
print(f'Dwójek wypadło: {x2}')
print(f'Trójek wypadło: {x3}')
print(f'Czwórek wypadło: {x4}')
print(f'Piątek wypadło: {x5}')
print(f'Szóstek wypadło: {x6}')