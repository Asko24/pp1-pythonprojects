print('Podaj długość bóków trójkąta: ')
a=int(input())
b=int(input())
c=int(input())

''' Warunek istnienia takiego trójkąta '''
if a<b<c and a+b<c:
        print('Podane długości boków nie mogą tworzyć trójkąta')
elif a<c<b and a+c<b:
        print('Podane długości boków nie mogą tworzyć trójkąta')
elif b<a<c and a+b<c:
        print('Podane długości boków nie mogą tworzyć trójkąta')
elif b<c<a and b+c<a:
        print('Podane długości boków nie mogą tworzyć trójkąta')
elif c<a<b and a+c<b:
        print('Podane długości boków nie mogą tworzyć trójkąta')
elif c<b<a and b+c<a:
        print('Podane długości boków nie mogą tworzyć trójkąta')
else:
    print('Z tych boków trójkąta można stworzyć trójkąt')
    
    p=(1/2)*(a+b+c)
    pole=(p*(p-a)*(p-b)*(p-c))**(1/2)
    print('Pole trójkąta wynosi: ',pole)