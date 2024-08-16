#Write a program that allows you to manage a company's customer database. The clients will be saved 
# in a dictionary in which the key of each client will be their NIF, and the value will be another 
# dictionary with the client's data (name, address, telephone, email, preferred), where preferred 
# will have the value True if This is a preferred customer. The program must ask the user for an 
# option from the following menu: (1) Add customer, (2) Delete customer, (3) Show customer, 
# (4) List all customers, (5) List preferred customers, (6) End . Depending on the option chosen, 
# the program will have to do the following:

#1.Ask for the customer's data, create a dictionary with the data and add it to the database.
#2.Ask for the client's NIF and delete their data from the database.
#3.Ask for the client's NIF and show their data.
#4.Show list of all clients in the database with their NIF and name.
#5.Show the list of preferred customers from the database with their NIF and name.
#6.Finish the program.

database={}
option=0

while option!=6:
    print("(1) Add customer")
    print("(2) Delete customer")
    print("(3) Show customer")
    print("(4) List all customers")
    print("(5) List preferred customers")
    print("(6) End")
    option=int(input("Introduce an option: "))
    if(option==1):
        nif=input("Introduce your NIF: ")
        
        name=input("Introduce your name: ")
        address=input("Introduce your address: ")
        phone=input("Introduce your telephone: ")
        mail=input("Introduce your email: ")
        preferred=input("Introduce True or False for being preferred: ")
        val={"name":name,"address":address,"phone":phone,"mail":mail,"preferred":preferred}
        database[nif]=val
    elif(option==2):
        nif=input("Introduce the nif of the client taht you want to delete: ")
        if nif in database:
            database.pop(nif)
        else:
            print("No client found with that nif")
    elif(option==3):
        nif=input("Enter the nif of the client you want to consult data about: ")
        if nif in database:
            print(database[nif])
        else:
            print("No costumer found with that nif")
    elif(option==4):
        if database:
            for i in database: 
                print(i+" -->"+database[i]["name"])
        else:
            print("No customers in the database")
        

    elif(option==5):
        for i in database:
            if(database[i]["preferred"]=="True"):
                print(i+" -->"+database[i]["name"])
    elif(option==6):
        print("Bye")
    else:
        print("Introduce a valid option")

