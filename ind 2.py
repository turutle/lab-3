# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:05:32 2021

@author: turtl
"""

import sys


if __name__ == '__main__':
    x = int(input("Введите первое число--> "))
    y = int(input("Введите второе число--> "))
    z = int(input("Введите третье число--> "))
    
    if x % 2 == 0:
        print("Первое число чётное")
    elif y % 2 == 0:
        print("Второе число чётное")
    elif z % 2 == 0:
        print("Третье число чётное")
        
    elif x % 2 == 1 or y % 2 == 1 or z % 2 == 1:
        print("Cреди чисел нет чётных")
    else:
        print("Ошибка!", file=sys.stderr)
        exit("Process finished with exit code 1")