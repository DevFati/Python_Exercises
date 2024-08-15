#Write a program that creates a dictionary simulating a shopping basket. The program must ask 
# for the item and its price and add the pair to the dictionary, until the user decides to finish. 
# Afterwards, the shopping list and the total cost must be displayed on the screen, with the following format

#Shopping list	
# Article 1    Price
# Article 2    Price
# Article 3    Price
# …              …
# Total        Cost

continuee=True
listt={}
summ=0
while continuee:
    item=input("Introduce an item: ")
    price=float(input("Introduce the price of "+item+": "))
    summ=summ+price
    listt[item]=price
    continuee=input("Do you want to continue? yes or no: ")=="yes"

print("Shopping list: ")
for i in listt:
    print(i+"         ",listt[i])

print("Total ",summ,"€")
