tab=[2, 3, 5, 2, 9, 8]# 1, 3, 9, 1, 1, 4, 7, 7, 1, 4, 4]

def mediana(liczby):
    liczby.sort()
    print(liczby)
    if (len(liczby)%2==1):
        med=liczby[int(len(liczby)/2)]
    else:
        med=(liczby[int(len(liczby)/2)]+liczby[int(len(liczby)/2)-1])/2
    print('Mediana: ',med)

mediana(tab)
        


