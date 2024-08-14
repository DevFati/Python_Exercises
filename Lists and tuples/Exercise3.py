#Write a program that stores the subjects of a course (for example Mathematics, Physics, Chemistry, 
# History and Language) in a list, asks the user the grade they have obtained in each subject, and 
# then displays them on the screen with the message In < subject> you have obtained <note> where <subject>
#  is each of the subjects in the list and <note> is each of the corresponding notes entered by the user.

subjects=["Mathematics","Physics","Chemistry","History","Language"]

marks=[]

for i in range(len(subjects)):

    mark=float(input("Introduce your mark in  "+subjects[i]+": "))
    marks.append(mark)

for i in range(len(subjects)):
    print("In "+subjects[i]+" you have obtained ",marks[i])

    