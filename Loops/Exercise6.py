#Write a program that asks the user for an integer number and displays on the screen a right triangle 
# with the height of the entered number.


number=int(input("Introduce an integer number: "))

for i in range(number):
  
    for j in range (i+1):
        print("*",end="")
    print("")
    
        
