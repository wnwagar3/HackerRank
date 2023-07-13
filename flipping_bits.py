'''
You will be given a list of 32 bit unsigned integers. Flip all the bits (1 --> 0 and 0 -- 1 ) and return the result as
an unsigned integer.

Example
n = 9 (base 10)
1001 = binary (base 2) resentation of 9.
We're working with 32 bits, so:
00000000000000000000000000001001 = 9
Flipped bits = 11111111111111111111111111110110 = 4294967286


Return 4294967286 .

Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer

Returns

int: the unsigned decimal integer result
Input Format

The first line of the input contains q, the number of queries.
Each of the next q lines contain an integer, n, to process.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    digits_lst = list(format(n, '032b'))
    for i in range(len(digits_lst)):
        if digits_lst[i] == '0':
            digits_lst[i] = '1'
        elif digits_lst[i] == '1':
            digits_lst[i] = '0'
    flipped_num = ''.join((j) for j in digits_lst)
    new_num = int(flipped_num, 2)
    return(new_num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
