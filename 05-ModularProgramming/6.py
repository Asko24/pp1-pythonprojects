import csv

tab=[]
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    j=0
    for line in f:
        if j==0:
            print('#')
            j+=1
        elif j==1:
            print('='*50)
            j+=1
        else:
            print(j-1)
            j+=1
'''
    for row in reader:
        for i in range (0,len(row)):



            if i==len(row)-1:
                print(row[i],end='\n')
            else:
                print(row[i],end='    ')
'''