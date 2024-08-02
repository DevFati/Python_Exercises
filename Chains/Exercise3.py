#Write a program that asks for the user's name in the console and after the user enters it, displays 
# <NAME> has <n> letters, where <NAME> is the username in uppercase and <n> is the number of letters 
# that have the name.


name=input("Give me your name: ")


print("<"+name.upper()+"> has ",len(name)," letters")