#The tax brackets for filing income in a given country are the following:

#Income                   Tax rate
#Less than €10,000            5%
#Between €10,000 and €20,000 15%
# Between €20,000 and €35,000 20%
# Between €35,000 and €60,000 30%
# More than €60,000           45%
# Write a program that asks the user their annual income and shows on the screen the tax rate that 
# corresponds to them.

b=float(input("Introduce your annual income: "))
c=0
if(b<10000):
    c=5
elif(b>=10000 and b<20000):
    c=15
elif(b>=20000 and b<35000):
    c=20
elif(b>=35000 and b<60000):
    c=30
else:
    c=45

print("You need to pay ",b*c/100,"€")
