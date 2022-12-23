t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums = []
    x = 1
    y = 0
    for m in range(n):
        y = y + x
        if y <= n and y % 2 ==0:
            nums.append(y)
        elif y > n:
            break
        x,y = y,x
    print(sum(nums))