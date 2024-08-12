#Write a program that asks the user for a word and displays it on the screen 10 times.

word=input("Introduce a word: ")

n=0
#1º way: 
while(n<10):
    print(word)
    n=n+1


#2º way:

for i in range(10):
    print(word)
