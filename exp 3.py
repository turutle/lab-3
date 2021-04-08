# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:40:06 2021

@author: turtl
"""

import math


if __name__ == '__main__':
    n = int(input("Value of n? "))
    x = float(input("Value of x? "))
    
    S = 0.0
    for k in range(1, n + 1):
        a = math.log(k * x) / (k * k)
        S += a
    print(f"S = {S}")