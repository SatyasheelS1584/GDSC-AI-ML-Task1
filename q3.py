n = int(input())

def m_fill(x):
    m = [""] * x
    for i in range(x):
        m[i] = input().split()
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m

m1 = m_fill(n)
m2 = m_fill(n)

m3 = [""] * n

for i in range(n):
    m3[i] = [""] * n
    for j in range(n):
        s = 0
        for k in range(n):
            s += (m1[i][k]*m2[k][j])
        m3[i][j] = s

a = 0
for k in range(n):
    a += m3[k][k]
print(a)