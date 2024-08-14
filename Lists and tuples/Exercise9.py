#Write a program that asks the user for a word and displays on the screen the number of times each vowel contains.

word=input("Introduce a word: ")

vowels=["a","e","i","o","u"]

word=word.lower()

for i in vowels:
    print("The vowel "+i+" appears ",word.count(i)," times")