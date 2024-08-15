#Write a program that asks the user for their name, age, address and telephone number 
# and saves it in a dictionary. Then you must display the message <name> is <age> years old, 
# lives at <address> and your phone number is <phone>.


age=int(input("Introduce your age: "))
name=input("Introduce your name: ")
address=input("Introduce your address: ")
telephone=input("Introduce your phone number: ")

person={"name":name,"age":age,"address":address,"telephone":telephone}

print(person["name"]," is ",person["age"]," years old, lives at ",person["address"]," and the phone number is ",person["telephone"])