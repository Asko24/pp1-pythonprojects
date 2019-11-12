nazwy=['Styczen','Luty','Marzec','Kwiecien','Maj','Czerwiec','Lipiec','Sierpien','Wrzesien','Pazdziernik','Listopad','Grudzien']

def nazwamiesiaca(x):
    if x<1 or x>12:
        print ('Wprowadzony numer miesiaca jest niepoprawny')
    else:
        print (f'{x} miesiac: {nazwy[x-1]}')

nazwamiesiaca(7)
nazwamiesiaca(9)