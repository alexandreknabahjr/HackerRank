#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    horas = s[0] + s[1]
    minutos = s[3] + s[4]
    segundos = s[6] + s[7]
    
    horasConvertidas = (int(s[0]) * 10) + int(s[1])
    
    novasHoras = 12 + ((int(s[0]) * 10) + int(s[1]))
    
    if "PM" in s:
        
        if(horasConvertidas >= 12):
            return(horas + ":" + minutos + ":" + segundos)
        else:
            if(novasHoras >= 24):
                return(str(novasHoras - 24) + ":" + minutos + ":" + segundos)
            else:
               return(str(novasHoras) + ":" + minutos + ":" + segundos)
    else:
        
        if(horasConvertidas < 12):
            return(horas + ":" + minutos + ":" + segundos)
        else:
            if(novasHoras >= 24):
                if((novasHoras - 24) < 10):
                    horasCertas = "0" + str(novasHoras - 24)
                else:
                    horasCertas = str(novasHoras - 24)
                    
                return(horasCertas + ":" + minutos + ":" + segundos)
            else:
               return(str(novasHoras) + ":" + minutos + ":" + segundos)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
