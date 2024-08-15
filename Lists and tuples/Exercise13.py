#Write a program that asks for a sample of numbers, separated by commas, saves them in a list, 
# and displays their mean and standard deviation on the screen.

numbers=input("Introduce numbers separated by commas: ")
numbers=numbers.split(",")
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

numbers=tuple(numbers)

sum=0
b=0

for i in numbers:
    sum=sum+i
    b=b+(i**2)

mean=sum/len(numbers)

stdev=(b/len(numbers)-mean**2)**(1/2)

print("Their mean is ",mean," and the standard deviation is ",stdev)