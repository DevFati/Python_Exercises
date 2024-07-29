#Write a program that asks the user for two integers and displays 
# on screen the <n> between <m> gives a quotient <c> and a remainder <r> where <n> and 
# <m> are the numbers entered by the user, and <c> and <r> are the quotient and 
# the rest of the entire division respectively.

m=int(input("Give me the first positive integer: "))
n=int(input("Give me the second positive integer: "))

print("The quotient between ",m, "and ",n," is ",(int((m/n)))," and the remainder is ",(m%n))