import random
x=random.randint(-50,50)
y=random.randint(-50,50)
p=f'P({x},{y})'

if x>=0 and y>=0:
    print(f'Punkt {p} znajduje się w pierwszej ćwiartce układu współrzędnych')
elif x>=0 and y<0:
    print(f'Punkt {p} znajduje się w drugiej ćwiartce układu współrzędnych')
elif x<0 and y>=0:
    print(f'Punkt {p} znajduje się w czwartej ćwiartce układu współrzędnych')
else:
    print(f'Punkt {p} znajduje się w trzeciej ćwiartce układu współrzędnych')