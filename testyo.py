#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:42:58 2020

@author: skayon
"""

hpmax = float(input("Give me max horsepower"))
flowload = float(input("Give me flowload"))
loadfactor = float(input("Give me load factor"))
motorefficiency = float(input("Give me motor efficiency"))
hplowload = hpmax*((flowload/60.0)**2.5)*(loadfactor/motorefficiency)
print("The Hp Low Load is " + str(hplowload))
kwhcost = hplowload * 0.746
print("The cost is " + str(kwhcost))