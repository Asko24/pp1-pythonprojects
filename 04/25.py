tab=['Janek','Ania','Wojtek','Zosia']

def jestimie(imie,imiona):
    check=0
    
    for i in range (0,len(imiona)):
        if imiona[i]==imie:
            check+=1
        
            
    if check>=1:
        print('Imie zawarte jest w wykazie imion')
    else:
        print('Imienia nie ma w wykazie imion')

x='Zosia'

print('Imiona: ',end='')
for i in range (0,len(tab)):
    print(tab[i],end=' ')
print('\nImie:',x)
jestimie(x,tab)
    
    