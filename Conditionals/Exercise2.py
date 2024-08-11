#Write a program that stores the "password" character string in a variable, asks the user for the password 
# and prints on the screen if the password entered by the user matches the one stored in the variable 
# without taking into account upper and lower case.

pas = "password"

password=input("Introduce your password: ")

password=password.lower()

if(pas==password):
    print("Correct")
else:
    print("Incorrect")