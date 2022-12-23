from math import *
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fi = (n-1)//15
    t = (n-1)//3
    f = (n-1)//5
    total = (3 * t * (t+1)//2) + (5 * f * (f+1)//2) - (15 * fi * (fi+1)//2)
    print(int(total))
    