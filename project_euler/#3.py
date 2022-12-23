t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    prime = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            prime.append(i)
        i = i + 1
    if n == 1:
        print(prime[-1])
    else:
        print(int(n))