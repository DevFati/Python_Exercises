#Write a program that asks the console for the products in a shopping cart, separated by commas, 
# and displays each of the products on the screen in a different line.

products=input("Introduce the products separated by a comma: ")

items=[str(i) for i in products.split(",")]

for i in items:
    print(i)