# There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of
# cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then
# sideLength[j] >= sideLength[i].
#
# When stacking the cubes , you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it
# is possible to stack the cubes. Otherwise, print No.
#
# Input Format
#
# The first line contains a single integer , the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains , the number of cubes.
# The second line contains  space separated integers, denoting the sideLengths of each cube in that order.
#
# Constraints:
#
# 1 <= T <= 5
# 1 <= n <= 10**5
# 1 <= sideLength < 2**31
#
# Output Format:
#
# For each test case, output a single line containing either Yes or No
# Sample Input
#
# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]
# Sample Output
#
# Yes
# No

T = int(input())  # Number of test cases

for _ in range(T):
    n = int(input())  # Number of cubes in the current test case
    blocks = list(map(int, input().split()))  # Length of each cube in the current test case
    left = 0  # Pointer to the leftmost cube
    right = n - 1  # Pointer to the rightmost cube
    valid = True  # Flag to indicate if the cubes can be stacked

    while left < right:
        if blocks[left] >= blocks[right]:
            a = blocks[left]  # Height of the current cube to be stacked
            left += 1  # Move the left pointer to the right
        else:
            a = blocks[right]  # Height of the current cube to be stacked
            right -= 1  # Move the right pointer to the left

        if blocks[left] > a or blocks[right] > a:
            valid = False  # If any cube is taller than the current cube to be stacked, stacking is not possible
            break

    if valid and blocks[left] <= a:
        print("Yes")  # All cubes have been successfully stacked in the required order
    else:
        print("No")  # Cubes cannot be stacked in the required order

