#Write a program that asks the user for an integer and displays a right triangle.

number=int(input("Introduce an integer: "))

for i in range(1,number+1,2):
    for j in range(i,0,-1):
        if(j%2!=0 ):
            print(j,end=" ")
    print("")