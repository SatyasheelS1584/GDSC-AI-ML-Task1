x = input()
l = [""]*int(x)
for i in range(len(l)):
    l[i] = input("").split()

for i in l:
    b = True
    for j in range(len(i[0])):
        if i[1].find(i[0][j]) == -1:
            b = False
            break
    if b:
        print("YES")
    else:
        print("NO")