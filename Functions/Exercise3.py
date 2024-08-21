#Write a function that takes a positive integer and returns its factorial.

def factorial(number):
    sum=1
    for i in range(number):
        sum*=i+1
    return sum

print(factorial(4))
print(factorial(20))
