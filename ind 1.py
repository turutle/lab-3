# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 22:23:58 2021

@author: turtl
"""

import sys


if __name__ == '__main__':
    x = int(input("По какой цене вы купили 8 рулонов(обоев)--> "))
    y = int(input("По какой цене вы купили 2 банки краски--> "))
    n = x + y
    
    if n > 200 and n < 500:
        print(n*0.97)
    elif n > 500 and n < 800:
        print(n*0.95)
    elif n > 800 and n < 1000:
        print(n*0.93)
    elif n > 1000:
        print(n*0.91)
    else:
        print("Ошибка!", file=sys.stderr)