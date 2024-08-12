#Write a program that asks the user for an amount to invest, the annual interest and the number of years, 
# and displays on the screen the capital obtained from the investment each year that the investment lasts.


money=float(input("Introduce the amount to invest: "))
interest=float(input("Introduce the annual interest: "))
years=int(input("Introduce the number of years: "))

for i in range(years):
    money*=1+interest/100
    print(money)