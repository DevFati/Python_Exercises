#Write a program that asks the user for two numbers and displays their division on the screen. 
# If the divisor is zero the program should display an error.

number1=int(input("Introduce the first number: "))

number2=int(input("Introduce the second number: "))

if(number2 == 0):
    print("error")
else:
    print(number1/number2)