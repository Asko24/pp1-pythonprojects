pin='0805'
proba=0
proba_max=3
pin_guess=0

while proba<proba_max:
    pin_guess=input('Podaj kod PIN: ')
    if pin_guess!=pin:
        print('Kod PIN niepoprawny')
        proba+=1
    else:
        break
if proba==proba_max:
    print('Karta płatnicza zostaje zablokowana.')
else:
    print('Poprawny kod PIN')

    