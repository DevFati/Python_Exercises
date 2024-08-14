#Write a program that asks the user for the winning numbers of the primitive lottery, stores 
# them in a list and displays them on the screen ordered from lowest to highest.

awarded=[]

for i in range(6):
    a=int(input("Introduce the winning numbers: "))
    awarded.append(a)

awarded.sort()

print("Thw winning numbers are: ",awarded)