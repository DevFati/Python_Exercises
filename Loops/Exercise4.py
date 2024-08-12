#Write a program that asks the user for a positive integer number and displays the countdown from that 
# number to zero separated by commas.

number=int(input("Introduce a positive integer number: "))

for i in range(number,-1,-1):
    print(i,end=",")


#for i in range(number, -1, -1):: This for loop loops through numbers starting from the value of the number 
# variable, up to and including 0, in steps of -1. This means that it decrements by 1 in each iteration.