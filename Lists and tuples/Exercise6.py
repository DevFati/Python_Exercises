#Write a program that stores the subjects of a course (for example Mathematics, Physics, Chemistry, 
# History and Language) in a list, asks the user the grade he/she received in each subject and
#  eliminates the approved subjects from the list. At the end, the program must display on the 
# screen the subjects that the user has to repeat.

subjects=["Mathematics","Physics","Chemistry","History","Language"]
#1º way: 
sub=[]
for i in range(len(subjects)):

    mark=float(input("Introduce your mark in  "+subjects[i]+": "))
    if(mark<5):
        sub.append(subjects[i])
  


print("You need to repeat the following subjects: ",sub)

#2º way: 

for i in range(len(subjects)-1,-1,-1):

    mark=float(input("Introduce your mark in  "+subjects[i]+": "))
    if(mark>=5):
        subjects.pop(i)
  


print("You need to repeat the following subjects: ",subjects)


#pop(i) removes the element at index i from the list.
#Avoiding Indexing Issues: By iterating from the end of the list to the beginning, the loop avoids the
#  pitfalls of forward iteration with removal. When an item is removed in reverse order, the subsequent 
# items that still need to be checked do not shift positions in a way that affects the remaining iterations.