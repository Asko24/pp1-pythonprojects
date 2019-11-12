tab=[]
with open ('numbers.txt','r') as file:
    for line in file:
        tab.append(int(line))

with open ('evennumbers.txt','w') as file2:
    for i in range (0,len(tab)):
        if tab[i]%2==0:
            file2.write(f'{tab[i]}\n')
        else:
            continue
