#Write a program that saves the prices of the fruits in the table in a dictionary, asks the user for a 
# fruit, a number of kilos, and displays the price of that number of kilos of fruit on the screen. 
# If the fruit is not in the dictionary, it should display a message informing you of this.

# Fruit     Price
# Banana    1.35
# Apple     0.80
# Pear      0.85
# Orange    0.70

shop={"Banana":1.35,"Apple":0.80,"Pear":0.85,"Orange":0.70}

fruit=input("Introduce a fruit: ")

kilos=float(input("Introduce number of kilos: "))

if(fruit in shop):
    print("The price of ",kilos,"kg of "+fruit+" is ",kilos*shop[fruit])
else:
    print("This fruit is not available")