#Write a program that displays the multiplication table from 1 to 10 on the screen.


for i in range(10):
    print("")
    print("Multiplication table of ",(i+1))
    for j in range(11):
       
        print((i+1),"*",j,"=",(i+1)*j)