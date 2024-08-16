#Write a program that manages a company's pending invoices. The invoices will be stored in a dictionary 
# where the key of each invoice will be the invoice number and the value will be the cost of the invoice. 
# The program should ask the user if they want to add a new invoice, pay an existing one, or end. If you 
# want to add a new invoice, it will ask for the invoice number and its cost and add it to the dictionary. 
# If you want to pay an invoice, you will be asked for the invoice number and it will be removed from the 
# dictionary. After each operation, the program must display on the screen the amount collected so far and 
# the amount pending collection.


bills={}

print("1: Add a new invoice")
print("2: Pay an existing one")
print("3: Finish")
option=input("Choose an option: ")
s=0
collect=0
while option!="3":
    if(option=="1"):
        num=input("Introduce the invoice number: ")
        cost=float(input("Introduce its cost: "))
        bills[num]=cost
        s=s+cost
    elif(option=="2"):
        n=input("Introduce the invoice number that you want to pay: ")
        cost=bills.pop(n,0)
        s=s-cost
        collect=collect+cost
       
    else:
        print("Introduce a valid option")
    print("The amount collected: ",collect)
    print("The amount pending collection: ",s)
    print("1: Add a new invoice")
    print("2: Pay an existing one")
    print("3: Finish")
    option=input("Choose an option: ")
