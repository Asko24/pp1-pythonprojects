import statistics

xyz=[21600, 4350, 3920, 5590, 3250, 4010]

print(f'Srednie wynagrodznie: {statistics.mean(xyz)}')
print(f'Mediana: {statistics.median(xyz)}')
print(f'Odchylenie standardowe: {statistics.pstdev(xyz)}')

