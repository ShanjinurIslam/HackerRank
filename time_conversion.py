#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    format = s[-2:]
    time = [int(x) for x in s[:-2].split(":")]

    if format == "PM":
        time[0] = (time[0]%12) + 12
    else:
        time[0] = time[0]%12

    final = (str(time[0]) if time[0]>=10 else "0"+str(time[0])) + ":" + (str(time[1]) if time[1]>=10 else "0"+str(time[1])) + ":" + (str(time[2]) if time[2]>=10 else "0"+str(time[2]))

    return final
    
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
