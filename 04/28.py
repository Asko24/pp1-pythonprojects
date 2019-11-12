lang=['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
procenty=[61,47,37,32,26,18,14,14,9,7]

def rysujWykres(jezyki,wartosci):
    for i in range (0,len(jezyki)):
            print('\n',jezyki[i],": ",wartosci[i]*"#",end='')

rysujWykres(lang,procenty)
