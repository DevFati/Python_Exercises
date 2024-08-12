#Write a program that stores the "password" string in a variable, prompting the user for the password 
# until the correct password is entered.

password="password"

key=input("Introduce the password: ")

while(key!=password):
    key=input("Introduce the password: ")