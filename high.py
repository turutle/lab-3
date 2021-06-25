# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 16:00:06 2021

@author: turtl
"""

import math

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Введите x--> "))
    
    if x < 0 or x > 2:
        print("Illegal value of x")
        exit("Process finished with exit code 1")
    else:
        a = 1 - x
        S = a
        k = 1
    
        while math.fabs(a) > EPS:
            a *= ((1 - x) * k**2) / (k + 1)**2
            S += a
            k += 1
            
        print(f"f({x}) = {S}")