#Write a program that asks the user for a word and shows on the screen if it is a palindrome.

word=input("Introduce a word: ")
#1º way: 

n=""
for i in range(len(word)-1,-1,-1):
    n=n+word[i]

if(word==n):
    print("Is a palindrome")
else:
    print("Is not a palindrome")

#2º way: 
n=word
n=list(n)
word=list(word)
n.reverse()
if(word==n):
    print("Is a palindrome")
else:
    print("Is not a palindrome")