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
    h24=''
    # Write your code here
    if s[-2] == 'P':
        hours = int(s[:2])+12
        if hours == 24:
            h24='12'+s[2:-2]
        else:
            h24=str(hours)+s[2:-2]
        return h24
    else:
        if int(s[:2]) != 12:
            return s[:-2]
        else:   
            h24 = '00'+s[2:-2]
            return h24

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

