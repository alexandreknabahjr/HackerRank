#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    
    candlesList = []
    candles.sort(reverse=True)
    
    for i in range(len(candles)):
        candlesList.append(candles[i])
        
    tallestCandle = candlesList.pop(0)
    candlesCount = 1
        
    for j in range(len(candlesList)):
        if(tallestCandle == candlesList[j]):
            candlesCount += 1
    
    return candlesCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
