#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    
    arr.sort(reverse=False)

    for i in range(len(arr) - 1):
        
        minSum += arr[i]
        
    arr.sort(reverse=True)
    
    for j in range(len(arr) - 1):
        
        maxSum += arr[j]
        
    print(minSum, maxSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
