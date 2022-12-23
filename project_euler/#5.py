t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    primes = [2]
    num = 1
    for i in range(3, n+1, 2):
        x = 2
        for j in range(2, i):
            if i % j != 0:
                x += 1
        if x == i:
            primes.append(i)
    for k in primes:
        j = 0
        while k ** j <= n:
            j += 1
        num *= (k**(j-1))
    print(num)