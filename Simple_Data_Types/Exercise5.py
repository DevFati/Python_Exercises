#Write a program that asks the user for the number of hours worked 
# and the cost per hour. Then you must display the payment that corresponds to you on the screen.

m=float(input("Hours worked: "))
n=float(input("Cost per hour: "))

print("The amount of the payment is : ",(m*n)," euros.")

#Note: You cannot concatenate "+" an int with a string, to do that you have to use ","