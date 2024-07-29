#Write a program that reads a positive integer, n,
#entered by the user and then displays the sum of all integers from 1 to n
# the sum of the first m  positive integers can be calculated as follows: sum= (n*(n+1)/2)


m=int(input("give me a positive integer: "))

if(m<=0):
    input("entered number less than or equal to 0")
else:
    input((m*(m+1))/2)
    