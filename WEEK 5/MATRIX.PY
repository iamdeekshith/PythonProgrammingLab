r=int(input("please enter the rows: "))
c=int(input("please enter the columuns: "))
m=[]
for i in range(r):
    row=[]
    for j in range(c):
        n=int(input("enter the numnber: "))
        row.append(n)
    m.append(row)
print(m)

m2=[]
for i in range(r):
    row=[]
    for j in range(c):
        n=int(input("enter the numnber: "))
        row.append(n)
    m2.append(row)
print(m2)

m3=[]
for i in range(r):
    row=[]
    for j in range(c):
        n=int(input("enter the numnber: "))
        sum = m[i][j]  + m2[i][j]
        row.append(sum)
    m3.append(row)
print(m3)

mul=[]
for i in range(r):
    row=[]
    for j in range(c):
        temp=0
        for k in range(r):
            temp += m[i][k] * m2[k][j]
        row.append(temp)
    mul.append(row)
print(mul)
    
    
