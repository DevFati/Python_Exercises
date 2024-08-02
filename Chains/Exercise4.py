#Business telephones have the following prefix-number-extension format where the prefix is ​
# ​the country code +34, and the extension is two digits (for example +34-913724710-56). Write 
# a program that asks for a phone number with this format and displays the phone number without 
# the prefix and extension.


phone_number=input("Introduce your phone number: ")

if(len(phone_number)==16 and (phone_number.count("+")==1 and phone_number.count("-")==2) ):
    print("valid format, the number is: "+phone_number[4:13])
else:
    print("invalid format")


#note: we can use [4:13] or [4:-3]