import re

cyfry=[]

with open ('land.txt','r') as file:
    for line in file:
        cyfry+=re.findall('\d',line)

suma=0

for i in range (0,len(cyfry)):
    suma+=int(cyfry[i])
    
print('Suma: ',suma)