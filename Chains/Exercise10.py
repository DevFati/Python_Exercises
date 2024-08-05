#Write a program that asks the console for the products in a shopping cart, separated by commas, 
# and displays each of the products on the screen in a different line.

products=input("Introduce the products separated by a comma: ")

#1º way: 

#This is a list comprehension that converts each element of the resulting list to a string (even though they are already 
# strings, this ensures that each element is treated as a string). Then, store these elements in the items list.
items=[str(i) for i in products.split(",")]

for i in items:
    print(i)

#2º way:

print(products.replace(",","\n"))


#3º way:

#The join() function takes a list of strings and joins them into a single string, with the specified separator between each element. 
# In this case, the separator is the newline character \n. This means that each list element will be joined with a line break between
#  them.
print("\n".join(products.split(",")))