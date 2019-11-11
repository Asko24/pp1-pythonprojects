nazwy_ocen=['niedostateczny','dopuszczający','dostateczny','dobry','bardzo dobry','celujący']
ocena=int(input('Podaj ocene: '))
if ocena>=1 and ocena<=6:
    print(f'Ocena słownie: {nazwy_ocen[ocena-1]}')
else:
    print('Podana ocena nie należy do przedziału 1 do 6')
    
    
'''dodałem if'a sprawdzającego czy ocena jest w poprawnym przedziale,
ponieważ przy wpisaniu np. 0 lub -2 odwoływaliśmy się do nazwy_ocen[-3]'''