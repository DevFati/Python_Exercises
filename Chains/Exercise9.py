#Write a program that asks the user the date of birth in dd/mm/yyyy format and displays the day, 
# month and year on the screen. Adapt the above program so that it also works when the day or 
# month is entered with a single character.

date=input("Introduce your date birth: ")

if(date.count("/")==2 and len(date.split("/")[0])==2 and len(date.split("/")[1])==2 and len(date.split("/")[2])==4):
    print("valid format. The day is ",date.split("/")[0]," , the month: ",date.split("/")[1]," and the year ",date.split("/")[2])
else:
    print("invalid format")


#Adapted way:_ 

if(date.count("/")==2 and (len(date.split("/")[0])==2 or len(date.split("/")[0])==1)  and (len(date.split("/")[1])==2 or len(date.split("/")[1])==1) and len(date.split("/")[2])==4):
    print("valid format. The day is ",date.split("/")[0]," , the month: ",date.split("/")[1]," and the year ",date.split("/")[2])
else:
    print("invalid format")