#Write a program that stores the vectors (1,2,3) and (-1,0,2) in two lists and displays their 
# dot product on the screen.

vector1=[1,2,3]
vector2=[-1,0,2]
r=0
for i in range(len(vector1)):
    r=r+vector1[i]*vector2[i]

print("The result is: ",r)