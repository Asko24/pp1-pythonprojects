def parzysta(x):
    return lambda x: True if x%2==0 else False

print(parzysta(5))