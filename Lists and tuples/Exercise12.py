#Write a program that stores the arrays in a list and display your product on the screen.
#Note: To represent matrices using lists, use nested lists, representing each row vector in a list.

a=((1,2,3),(4,5,6))

b=((-1,0),(0,1),(1,1))

r=[[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            r[i][j]+=a[i][k]*b[k][j]


for i in range (len(r)):
    r[i]=tuple(r[i])


for i in range(len(r)):
    print(r[i])