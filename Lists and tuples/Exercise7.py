#Write a program that stores the alphabet in a list, eliminates from the list the letters that 
# occupy positions multiples of 3, and displays the resulting list on the screen.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(len(alphabet),1,-1):
    if(i%3==0):
        alphabet.pop(i-1)

print(alphabet)
