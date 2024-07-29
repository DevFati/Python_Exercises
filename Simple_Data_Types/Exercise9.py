#Write a program that asks the user for an amount to invest, 
# the annual interest and the number of years, and show on the screen the capital obtained from the investment.

m=float(input("Enter amount to invest: "))
n=float(input("Enter the annual interest: "))
f=int(input("Enter the number of years: "))

print("The capital obtained in the investment is: ",(round((m*(n/100+1)**f),2)))