tab=[]
with open ('universities.txt','r') as file:
    for line in file:
        tab.append(line)

tab2=sorted(tab)

with open ('universitiesalphabetically.txt','w') as file2:
    for i in range (0,len(tab2)):
        file2.write(f'{tab2[i]}\n')
        i+=1