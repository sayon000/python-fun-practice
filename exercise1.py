#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they
#will turn 100 years old.

name = input("Give me your name: ")
age = input("Give me your age: ")
print("Hello " + name + ", you are currently " + age + " years old.")
yearsFromHundred = 100 - int(age)
hundredYearsStatement = "You are " + str(yearsFromHundred) + " years away from being 100. \n" 
print(hundredYearsStatement)
numRepeat = int(input("Tell me how many times you want to repeat the previous message: "))
print(hundredYearsStatement * numRepeat)
