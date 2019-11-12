def potega(x,n):
    if x==0:
        return 0
    if n==0:
        return 1
    if x==1:
        return 1
    if x>1 and n>0:
        return x*x**(n-1)
    
print(f'5 do potegi 3 wynosi {potega(5,3)}')
        