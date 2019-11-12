tab=[]
with open ('numbers.txt','r') as file:
    for line in file:
        tab.append(int(line))

tab.sort()
print(tab)
        
    
    