#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input().strip())
def run(n):
    if n%2 != 0:
        print ("Weird")
    if n%2 == 0 and 2 <= n <= 5:
        print ("Not Weird")
    if n%2 == 0 and 6 <= n <= 20:
        print ("Weird")
    if n%2 == 0 and n > 20:
        print ("Not Weird")
        
if __name__ == '__main__':
    run (n)
    