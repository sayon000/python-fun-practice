#Write a program that returns a list that contains only the elements
#that are common between the lists (without duplicates). Make sure your
#program works on two lists of different sizes.

import random as rand
import time as t

rand.seed(t.gmtime())

a = []
b = []
c = []

for x in range(rand.randint(1,50)):
    a.append(rand.randint(0,10))

for x in range(rand.randint(1,50)):
    b.append(rand.randint(0,10))

for x in a:
    if x in b and x not in c:
        c.append(x)

print(a)
print(b)
print(c)
