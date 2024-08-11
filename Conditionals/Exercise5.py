#To pay a certain tax you must be over 16 years old and have income equal to or greater than €1,000 per month. 
# Write a program that asks the user their age and monthly income and shows on the screen whether the user 
# has to pay taxes or not.


age=int(input("Introduce your age: "))

income=float(input("Introduce your monthly income: "))

if(age>16 and income >=1000):
    print("You need to pay taxes")
else:
    print("You dont need to pay taxes")