n = (int(input('Podaj ilość liczb pierwszych: ')))
primes = []
count = 0
possiblePrime = 1
while possiblePrime > 0:
    possiblePrime += 1
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    if isPrime:
        primes.append(possiblePrime)
        count += 1
        if count == n:
            break

print(primes)