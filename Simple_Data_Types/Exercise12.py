#A bakery sells loaves of bread for €3.49 each. Bread that is not the same day has a 60% discount. 
# Write a program that starts by reading the number of bars sold that are not of the day. After the 
# program should show the usual price of a loaf of bread, the discount given for not being 
# fresh and the total final cost.

barrasN=(int(input("Enter the number of bars that are not of the day: ")))

print("The loaves of bread normally cost 3.49 each, so the total in that case would be ",round((3.49*barrasN),2)," euros.")
print("Since it is not fresh, a 60% discount is given, so it would have a discount of ",round((barrasN*3.49*0.6),2)," euros")
print("The final price would be: ",round((barrasN*3.49*0.4),2))