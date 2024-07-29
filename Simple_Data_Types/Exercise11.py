#Imagine that you have just opened a new savings account that offers you 4% interest per year. 
# These savings due to interest, which are not collected until the end of the year, are added to your balance
# end of your savings account. Write a program that starts by reading the amount of money 
# deposited in the savings account, entered by the user. Then the program must calculate 
# and display on the screen the amount of savings after the first, second and third years. Round each
# quantity to two decimal places.

money=float(input("Enter amount of money deposited in the account: "))
interest1=1.04*money
print("Savings after 1 year: ",round(interest1,2), " euros")
interest2=interest1*1.04
print("Savings after 2 years: ",round(interest2,2), " euros")
interest3=interest2*1.04
print("Savings after 3 years: ",round(interest3,2), " euros")

