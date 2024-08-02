#Write a program that asks the user to enter a phrase into the console and displays the inverted 
# phrase on the screen.


phrase= input("Introduce a sentence: ")

print("The inverted sentence is: "+phrase[::-1])


#The segmentation syntax in Python is [start:end:step]. If you omit start and end, Python assumes 
# you want to work with the entire string. The step indicates how to move through the chain.
#Step is -1, which indicates that the chain will be traversed backwards, that is, from the end to the beginning.