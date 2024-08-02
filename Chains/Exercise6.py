#Write a program that asks the user to enter a phrase into the console and a vowel, 
# and then displays the same phrase on the screen but with the vowel entered in capital letters.

phrase= input("Give me a sentence: ")

vowel=input("Introduce a vowel: ")

print(phrase.replace(vowel,vowel.upper()))