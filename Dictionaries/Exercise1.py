#Write a program that stores the dictionary {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} in a variable, 
# asks the user for a currency and displays its symbol or a message. notice if the currency is 
# not in the dictionary.

b={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

currency=input("Introduce a currency: ")

#1º way: 
print(b.get(currency.title(),"The currency is not here"))

#2º way: 
if currency.title() in b:
    print(b[currency.title()])
else:
    print("The currency is not here")