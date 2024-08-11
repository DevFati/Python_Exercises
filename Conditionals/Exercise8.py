#In a certain company, its employees are evaluated at the end of each year. The points they can obtain 
# in the evaluation start at 0.0 and can increase, translating into better benefits. The points that 
# employees can earn can be 0.0, 0.4, 0.6 or more, but not intermediate values ​​between the mentioned 
# figures. Below is a table with the levels corresponding to each score. The amount of money earned in
#  each level is €2,400 multiplied by the level score.

#Level            Score
#Unacceptable      0.0
#Acceptable        0.4
# Meritorious      0.6 or more

# Write a program that reads the user's score and indicates their level of performance, as well 
# as the amount of money the user will receive.


b=float(input("Introduce your score: "))

if(b==0.0):
    print("Your level of performance is unacceptable and the amount of money that u will receive is: ",b*2400)
elif(b==0.4):
    print("Your level of performance is acceptable and the amount of money that u will receive is: ",b*2400)
elif(b>=0.6):
    print("Your level of performance is meritorious and the amount of money that u will receive is: ",b*2400)
