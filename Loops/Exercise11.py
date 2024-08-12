#Write a program that asks the user for a word and then displays the letters of the entered 
# word one by one on the screen, starting with the last one.

word=input("Introduce a word: ")

for i in range(len(word)-1,-1,-1):
    print(word[i])