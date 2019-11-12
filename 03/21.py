tab=[]
with open ('numbersinrows.txt','r') as file:
    for line in file:
        x=line.split(',')
        tab+=x
    
suma=0
for i in range (0,len(tab)):
    suma+=int(tab[i])
print('Ilość liczb: ',len(tab))    
print('Suma: ',suma)
