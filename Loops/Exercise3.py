#Write a program that asks the user for a positive integer and displays all odd numbers from 1 to that number
#  separated by commas.

number=int(input("Introduce a positive integer: "))

#1º way: 

for i in range(number):
    if((i+1)%2!=0):
        print(i+1,end=",")

#2º way: 

for i in range(1, number+1, 2):
    print(i, end=", ")

# for i in range(1, n+1, 2):: This line starts a for loop that loops through numbers starting at 1 until 𝑛+1
#n+1 (not inclusive), increasing in steps of 2. This means it will take the numbers 1, 3, 5, etc.

#print(i, end=", "): Inside the loop, the value of i is printed, followed by a comma and a space. 
# The end=", " argument causes a comma to be added after each printed number instead of a line break.