with open ('students.txt','r') as file:
    for line in file:
        x=line.split(',')
        if x[2]!='age':
            if int(x[2])<30:
                print(line)
