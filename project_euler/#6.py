t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sqsum = n*(n+1)*(2*n+1)/6
    summ = (n*(n+1)/2)**2
    print(int(summ - sqsum))