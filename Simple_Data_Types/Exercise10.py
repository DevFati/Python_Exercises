#A toy store is very successful in two of its products: clowns and dolls. 
# They usually sell by mail and the logistics company charges them by weight 
# of each package so you must calculate the weight of the clowns and dolls 
# that will appear in each package on demand. Each clown weighs 112 g and each doll 75 g. 
# Write a program that reads the number of clowns and dolls sold in the last
# order and calculate the total weight of the package that will be sent.


doll=int(input("Enter the number of dolls sold: "))
clown=int(input("Enter the number of clowns sold: "))

print("The package sent will have a total weight in grams of ",round((doll*75+clown*112),2))