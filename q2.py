n = int(input())
c = 1
for i in range(n):
    for j in range(i+1):
        if c > 5:
            c = 1
        print(c, end = "")
        c += 1
    print()