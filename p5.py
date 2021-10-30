# -*- coding: utf-8 -*-

__author__ = "Swetank Subham"
__credits__ = "Swetank Subham"
__license__ = "GPL"

__maintainer__ = "Swetank Subham"
__website__ = "https://swetanksubham.com/"

"""
PROBLEM: Print below mentioned pattern:
******
*****
****
***
**
*
"""

# START: SOLUTION 1
def print_pattern_solution_1():
    height = 6
    for i in range(height):
        for j in range(height - i):
            print("*", end="")
        print()

# Executed 10000 time in 0.23852133750915527 second(s).
# END: SOLUTION 1


# START: SOLUTION 2
def print_pattern_solution_2():
    height = 6
    for i in range(height):
        print("*" * (height - i))

# Executed 10000 time in 0.10698676109313965 second(s).
# END: SOLUTION 2

if __name__ == "__main__":
    print_pattern_solution_1()
    print_pattern_solution_2()