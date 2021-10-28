# -*- coding: utf-8 -*-

__author__ = "Swetank Subham"
__credits__ = "Swetank Subham"
__license__ = "GPL"

__maintainer__ = "Swetank Subham"
__website__ = "https://swetanksubham.com/"

"""
PROBLEM: Print below mentioned pattern
*****
*****
*****
"""

# START: SOLUTION 1
def print_pattern_solution_1():
    for i in range(3):
        for i in range(5):
            print('*', end='')
        print()

# Executed 10000 time in 0.14913582801818848 second(s).
# END: SOLUTION 1


# START: SOLUTION 2
def print_pattern_solution_2():
    for i in range(3):
        print('*'*5)

# Executed 10000 time in 0.054048776626586914 second(s).
# END: SOLUTION 2

if __name__ == '__main__':
    print_pattern_solution_1()
    print_pattern_solution_2()
