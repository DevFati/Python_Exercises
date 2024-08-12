#Write a program that asks the user for an integer and shows on the screen whether it is a prime number or not.

number=int(input("Introduce an integer: "))
h=0
for i in range(1,number+1):
    if(number%i==0):
        h=h+1

if(h==2 ):
    print("The number is  prime")
else:
    print("Is not a prime number")