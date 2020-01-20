#Ask the user for a number. Depending on whether the number is even or odd,
#print out an appropriate message to the user.

number = int(input("Friend, give me a number: "))
if number % 2: ###Number is odd
    print(str(number) + " is an odd number")
else:
    print(str(number) + " is an even number")
