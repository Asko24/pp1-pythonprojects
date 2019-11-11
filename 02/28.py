a=4
b=15

for i in range (0,b):
    if i==b-1:
        print('*',end='\n')
    else:
        print('*',end='')
for j in range (0,a-2):
    print('*',end='')
    print(' '*(b-2),end='')
    print('*')
for k in range (0,b):
    print('*',end='')