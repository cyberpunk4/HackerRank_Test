# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Difficulty: Easy
# Score: 10

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    '''if n % 2 == 0 and n in range(2,6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6,21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Weird")'''
    # this is a short and smart way of doing things
    print("Weird" if n % 2 == 1 or n in range(6,21) else "Not Weird")

    ''' Also without if else '''
    '''check = {True: "Not Weird", False: "Weird"}
    print(check[
              n % 2 == 0 and (
                      n in range(2, 6) or
                      n > 20)
              ])'''
    ''' also with another method'''
    '''check = {True: "Weird", False: "Not Weird"}

    print(check[
              n % 2 == 1 or n in range(6, 21)])'''