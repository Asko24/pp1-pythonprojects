wspolczynniki=[]
def czytajWspolczynniki():
    a=float(input('Wprowadz wspolczynnik a: '))
    wspolczynniki.append(a)
    b=float(input('Wprowadz wspolczynnik b: '))
    wspolczynniki.append(b)
    c=float(input('Wprowadz wspolczynnik c: '))
    wspolczynniki.append(c)

#sprawdzenie
#czytajWspolczynniki()
#print(wspolczynniki)

delta=[]
def obliczDelte():
    delta.append(wspolczynniki[1]**2-4*wspolczynniki[0]*wspolczynniki[2])
    print(delta)


#sprawdzenie
#obliczDelte(wspolczynniki[0],wspolczynniki[1],wspolczynniki[2])
#print('Delta: ',delta)

pierwiastki=[]
def obliczPierwiastki():
    if delta[0]==0.0:
        x1=-1*wspolczynniki[1]/2*wspolczynniki[0]
        pierwiastki.append(x1)
    elif delta[0]>0.0:
        x1=(-1*wspolczynniki[1]-delta[0]**(1/2))/(2*wspolczynniki[0])
        x2=(-1*wspolczynniki[1]+delta[0]**(1/2))/(2*wspolczynniki[0])
        pierwiastki.append(x1)
        pierwiastki.append(x2)
    else:
        deltaujemna='Delta ujemna. Brak rozwiazan w zbiorze liczb rzeczywistych'
        pierwiastki.append(deltaujemna)

#sprawdzenie
#obliczPierwiastki(wspolczynniki[0],wspolczynniki[1],wspolczynniki[2])
#print(pierwiastki)
       
        
def wyswietlPierwiastki():
    print('Pierwiastki: ',end='')
    for i in range (0,len(pierwiastki)):
        print(pierwiastki[i],end='  ')

#sprawdzenie
#wyswietlPierwiastki()


czytajWspolczynniki()
obliczDelte()
obliczPierwiastki()
wyswietlPierwiastki()