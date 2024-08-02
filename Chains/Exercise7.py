#Write a program that asks for the user's email in the console and displays another 
# email with the same name (the part in front of the @) but with the domain ceu.es.

email=input("Introduce your mail: ")

#1º way: 

print("The email with the new domain is: "+email.split("@")[0]+"@ceu.es")

#2º way: 

print(email[:email.find("@")]+"@ceu.es")

#email.find('@'):
#This part of the code looks for the position of the '@' character in the email string.