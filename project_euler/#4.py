t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest_pal = [] 
    for i in range(n-(n % 11), 101100, -11):
        if largest_pal:
                break
        if str(i) == str(i)[::-1]:
            for j in range(999, 317, -1):
                if i % j == 0 and len(str(int(i/j))) == 3:
                    largest_pal.append(i)
                    break     
    print(largest_pal[0])