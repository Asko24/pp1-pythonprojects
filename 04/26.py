def podatek(dochod):
    if dochod<=5000:
        return 0.17*dochod
    else:
        return 0.32*(dochod-5000)+0.17*5000

dochod=int(input('Podaj dochod: '))
print('Podatek należny: ',podatek(dochod))