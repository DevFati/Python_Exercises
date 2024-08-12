#Write a program in which the user is asked for a phrase and a letter, and displays on the screen 
# the number of times the letter appears in the phrase.

phrase=input("Introduce a phrase: ")

letter=input("Introduce a letter: ")

#1º way: 
print("The letter "+letter+" appears ",phrase.count(letter)," times in the phrase")

#2º way: 
c=0
for i in phrase:
    if(i==letter):
        c=c+1

print("The letter "+letter+" appears ",c," times in the phrase")
