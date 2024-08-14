#Write a program that stores the following prices in a list, 50, 75, 46, 22, 80, 65, 8, and displays
#  the lowest and highest of the prices on the screen.

prices=[50, 75, 46, 22, 80, 65, 8]

prices.sort()

print("The lowest is ",prices[0]," and the highest is ",prices[len(prices)-1])