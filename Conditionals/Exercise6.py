#The students of a course have been divided into two groups A and B according to sex and name. Group A 
# is made up of women with a name before M and men with a name after N and group B for the rest. Write 
# a program that asks the user for their name and gender, and displays the group that corresponds to 
# them on the screen.


name=input("Introduce your name: ")
gender=input("Introduce your gender: ")
name=name.lower()
if((gender=="women" and (name[0]>="a" and name[0]<="m")) or (gender=="men" and (name[0]>="n" and name[0]<="z"))):
    print("You belong to the A group")
else:
    print("You belong to the B group")