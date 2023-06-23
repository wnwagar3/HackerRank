# A newly opened multinational brand has decided to base their company logo on the three most common characters in
# the company name. They are now trying out various combinations of company names and logos based on this condition.
# Given a string , which is the company name in lowercase letters, your task is to find the top three most common
# characters in the string.
#
# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
#
# For example, according to the conditions described above,
# GOOGLE would return the 3 letters G O E
#
#
# Input Format
# A single line of input containing the string .
#
# Constraints
# 3 < len(s) <= 10**4
# s has at least  distinct characters
# Output Format
#
# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
#
# Sample Input 0
#
# aabbbccde

# Sample Output 0
#
# b 3
# a 2
# c 2

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    counts = {}

    for letter in s:
        counts[letter] = counts.get(letter, 0) + 1

    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    for item in sorted_counts[:3]:
        print(item[0], item[1])

