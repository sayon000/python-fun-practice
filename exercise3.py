#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less
#than 5.
#[output] for [item] in [list] if [filter]

import random as rand
import time as t

rand.seed(t.gmtime())

a = []



for x in range(rand.randint(1,100)):
    a.append(rand.randint(0,1000))

upperBound = int(input("We made a random list of numbers. Give me the max you want: "))

print([num for num in a if num < upperBound])
