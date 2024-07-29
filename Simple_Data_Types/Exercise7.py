#Write a program that asks the user for their weight (in kg) and height (in meters), 
# calculate body mass index and store it in a variable, and display by 
# display the phrase Your body mass index is <bmi> where <bmi> is the index of
# calculated body mass rounded to two decimal places.

m=float(input("Give me your weight in kg: "))

f=float(input("Give me your height in meters: "))

g=m/(f ** 2)

input(round(g,2))