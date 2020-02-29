#Ask the user for a string and print out whether this string is a palindrome
#or not. (A palindrome is a string that reads the same forwards and backwards.)

check = input("Give me a word to check: ")
stringLength = len(check)
isPalindrome = False

def isPalindrome(p):
    for i in range(0,int(stringLength/2)):
        if check[i] != check[stringLength-i-1]:  #REMEMBER minus 1 for string length
            return False
    return True


if isPalindrome(check):
    print(check + " is a palindrome")
else:
    print(check + " is not a palindrome")
    
