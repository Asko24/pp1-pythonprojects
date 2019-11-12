n=0
with open ('NoEducation.txt','r') as file:
    for line in file:
        print (1+n,'. ', end='')
        print (line, end='')
        n+=1
        