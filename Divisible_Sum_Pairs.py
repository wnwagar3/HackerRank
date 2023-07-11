#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    counter = 0 # initialize counter
    for i in range(len(ar)): # start looping at index 0 and go until the end of list/array
        for j in range(i + 1, len(ar)): # start from i + 1 and loop thru rest of list/array
            if ((ar[i] + ar[j]) % k) == 0: # if the array index values (i,j) summed together are divisible by k
                counter += 1 # increment the counter by 1
    return counter # return the counter variable which contains an int of how many pairs are divisible by k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()