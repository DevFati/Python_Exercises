#Write a program that asks the console for the user's name and a number
# integer and print the user's name on different lines on the screen as many 
# times as the number entered.


m=input("Introduce your name: ")
number=int(input("Introduce a positive integer: "))
#1º way
n=0

while n!=number:
    print(m)
    n=n+1

#2º way

print((m+"\n")*n)