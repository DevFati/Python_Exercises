#Write a program that stores the dictionary with the credits of the subjects of a course 
# {'Mathematics': 6, 'Physics': 4, 'Chemistry': 5} and then displays the credits of each subject 
# on the screen in the format <subject > has <credits> credits, where <subject> is each of the subjects 
# in the course, and <credits> are its credits. At the end it must also show the total number of credits 
# for the course.

a={'Mathematics': 6, 'Physics': 4, 'Chemistry': 5}
s=0
for i in a:
    print(i, "has ",a[i]," credits")
    s=s+int(a[i])

print("The total number of credits is ",s)