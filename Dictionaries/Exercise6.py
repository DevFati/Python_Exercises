#Write a program that creates an empty dictionary and fills it with information about a 
# person (for example name, age, gender, phone number, email, etc.) that is requested 
# from the user. Every time new data is added, the contents of the dictionary must be printed.

c=True
a={}

while c:
    key=input("What type of data do you want to add?: ")
    value=input(key +": ")
    a[key]=value
    print(a)
    c=input("Do you want to continue? Introduce True or False: ")=="True"


#After receiving input from the user, this line compares the input to the string "True".