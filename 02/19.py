n=int(input('Podaj n: '))

print('Ciąg arytmetyczny o różnicy 3:',end=' ')
x=1
print(x,end=', ')
for i in range (1,n+1):
    if i==n:
        x+=3
        print(x,end='')
    else:
        x+=3
        print(x,end=', ')