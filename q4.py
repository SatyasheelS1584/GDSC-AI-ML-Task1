n = int(input())

s = [""]*n

for i in range(n):
    x = input()
    while len(x) != 0 and int(x[0]) + int(x[len(x) - 1]) == 1:
        x = x[1:len(x) - 1]
    s[i]= len(x)

for i in s:
    print(i)