# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:31:56 2021

@author: turtl
"""

import math


if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x <= 0:
        y = 2 * x * x + math.cos(x)
    elif x < 5:
        y = x + 1
    else:
        y = math.sin(x) - x * x
    print(f"y = {y}")