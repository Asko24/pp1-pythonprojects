fib = 50
n1 = 0
n2 = 1
liczba = 0
while liczba < fib:
    print(n1,end=' , ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    liczba += 1 