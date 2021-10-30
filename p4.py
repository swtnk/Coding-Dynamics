# -*- coding: utf-8 -*-

__author__ = "Swetank Subham"
__credits__ = "Swetank Subham"
__license__ = "GPL"

__maintainer__ = "Swetank Subham"
__website__ = "https://swetanksubham.com/"

"""
PROBLEM: Print below mentioned pattern:
*
**
***
****
*****
******
"""

# START: SOLUTION 1
def print_pattern_solution_1():
    for i in range(6):
        for j in range(i+1):
            print("*", end="")
        print()

# Executed 10000 time in 0.24402856826782227 second(s).
# END: SOLUTION 1


# START: SOLUTION 2
def print_pattern_solution_2():
    for i in range(6):
        print("*" * (i+1))

# Executed 10000 time in 0.10558485984802246 second(s).
# END: SOLUTION 2

if __name__ == "__main__":
    print_pattern_solution_1()
    print_pattern_solution_2()
