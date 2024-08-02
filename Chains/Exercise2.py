#Write a program that asks the user's full name at the console and then displays the user's 
# full name three times, once with all lowercase letters, once with all uppercase letters, 
# and once with only the first letter of the name and surnames in capital letters. The user 
# can enter their name combining upper and lower case as they wish.


name =input("Give me your full name: ")

print(name.lower())
print(name.upper())
print(name.title())