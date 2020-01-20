#Ask the user for a number. Depending on whether the number is even or odd,
#print out an appropriate message to the user.
#Ask the user for two numbers: one number to check (call it num) and one
#number to divide by (check). If check divides evenly into num, tell that
#to the user. If not, print a different appropriate message.

num = int(input("Friend give me a number you want to check for complete division: "))
check = int(input("Friend give me the check number: "))
if(num % check == 0):
    print(str(num) + " is divisible by " + str(check))
else:
    print(str(num) + " is not divisible by " + str(check))
