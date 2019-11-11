imiona=['Genowefa','Onufry','Celestyna','Alojzy','Pankracy','Teofil']
longest=''


for i in range (0,len(imiona)):
    if len(imiona[i])>len(longest):
        longest=imiona[i]
    else:
        continue

print('Najdłuższe imie: ',longest)
