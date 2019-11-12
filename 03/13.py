tab=[32,16,5,8,24,7]
with open ('Tablica.txt','w') as file:
    for i in range (0,len(tab)):
        file.write(f'{str(tab[i])}\n')
        i+=1