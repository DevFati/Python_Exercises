#Write a program that creates a Spanish-English translation dictionary. The user will enter the words in 
# Spanish and English separated by colons, and each <word>:<translation> pair separated by commas. 
# The program must create a dictionary with the words and their translations. Then you will ask for
#  a phrase in Spanish and use the dictionary to translate it word by word. If a word is not in the
#  dictionary you must leave it untranslated.

dicti={}
c=True
words=input("Introduce a list of words and translations in the format word:translation separated by colons: ")

for i in words.split(","):
    key,value=i.split(":")
    dicti[key]=value


phrase=input("Introduce a phrase that you want to be translated: ")


for i in dicti:
    if(phrase.count(i)>=1):
        phrase=phrase.replace(i,dicti[i])

print(phrase)