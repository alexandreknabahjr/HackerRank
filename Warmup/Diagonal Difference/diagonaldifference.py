#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    right = 0
    left = 0
    k = len(arr) - 1
    
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            
            if(i == j):
                
                right += arr[i][j]
     
                
    for m in range(len(arr)):

        for n in range(len(arr)):

            if(n == k):

                left += arr[m][n]
        
        k -= 1
        
    return abs(right - left)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
