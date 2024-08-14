#Write a program that stores the subjects of a course (for example Mathematics, Physics, Chemistry, 
# History and Language) in a list and displays the message I study <subject> on the screen, where <subject> 
# is each of the subjects of the list.


subjects=["Mathematics","Physics","Chemistry","History","Language"]

# 1º way: 
for i in range(len(subjects)):
    print("I study "+subjects[i])

#2º way: 

for a in subjects:
    print("I study "+a)