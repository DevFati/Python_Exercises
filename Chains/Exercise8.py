#Write a program that asks the console for the price of a product in euros with two decimal places
# and displays on the screen the number of euros and the number of cents of the entered price.

price=input("Introduce the price with two decimals: ")


if(price.count(".")==1 and len(price.split(".")[1])==2):
    #1º way: 
    print("valid format, the price is ",price.split(".")[0]," euros and ",price.split(".")[1]," cents")
else:
    print("invalid format")


#2º way: 
print(price[:price.find('.')], 'euros y', price[price.find('.')+1:], 'cents.')