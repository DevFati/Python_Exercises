#Write a program that stores the numbers 1 to 10 in a list and displays them on the screen in reverse 
# order separated by commas.

numbers=[1,2,3,4,5,6,7,8,9,10]

#1º way: 

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i],end=",")

#2º way: 

for i in range(1, 11):
    print(numbers[-i], end=", ")

#numbers[-i] accesses the elements from the end of the list.

#3º way: 

numbers.reverse()
for number in numbers:
    print(number, end=", ")

#numbers.reverse() reverses the order of the elements in the list numbers in place. This means that
#  the original list is modified to have its elements in the opposite order.