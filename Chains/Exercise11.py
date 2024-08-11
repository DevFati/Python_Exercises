#Write a program that asks for the name of a product, its price and a number of units and displays 
# on the screen a string with the name of the product followed by its unit price with 6 integer digits 
# and 2 decimals, the number of units with three digits and the total cost with 8 whole digits and 2 decimals.


name=input("Introduce the name of the product: ")
price=float(input("Introduce the price: "))
units=int(input("Introduce number of units: "))

print("The product "+name+ ". Each unit costs "+"{:09.2f}".format(price)+" euros. The number of units is {:03}".format(units)+". The final cost is {:011.2f}".format(price*units))

#The 0 is put in front of the 9 so that the missing spaces are filled with 0. It is put in 9 because there are 6 digits plus 2 decimals plus the comma, which makes them 9.