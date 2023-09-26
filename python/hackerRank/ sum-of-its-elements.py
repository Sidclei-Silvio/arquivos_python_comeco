#!/bin/python3

import math
import os
import random
import re
import sys

# 1 lê o array
# somar os elementos
# Imprimir os elementos

def simpleArraySum(ar):
 count= 0
 for i in ar:
  count = count + i
 print (count)  


if __name__ == '__main__':
 arr = [1,2,3,4,5,6,7,8,9]
 value = simpleArraySum(arr)
 print(value)