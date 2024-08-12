#Write a program that echoes everything the user enters until the user types “exit” which will end.

while True:
    phrase=input("Introduce sentences: ")

    if(phrase=="exit"):
        break
    print(phrase)