#Write a program that asks for a date in dd/mm/yyyy format and displays the same date on 
# the screen in dd format of <month> of yyyy where <month> is the name of the month.

months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August' , 9:'September', 10:'October', 11:'November', 12:'December'}
date=input("Introduce a date with the following format (dd/mm/yyyy): ")

date=date.split("/")

a={"day":date[0],"month":date[1],"year":date[2]}

print(a['day']," of ",months[int(a['month'])], " of ",a['year'])