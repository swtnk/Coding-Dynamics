# -*- coding: utf-8 -*-

__author__ = "Swetank Subham"
__credits__ = "Swetank Subham"
__license__ = "GPL"

__maintainer__ = "Swetank Subham"
__website__ = "https://swetanksubham.com/"

"""
PROBLEM: Print below mentioned pattern
*****
*   *
*   *
*****
"""

# START: SOLUTION 1
def print_pattern_solution_1():
    for i in range(4):
        for j in range(5):
            if i not in (0, 3) and j not in (0, 4):
                print(' ', end='')
            else:
                print('*', end='')
        print()

# Executed 10000 time in 0.21051025390625 second(s).
# END: SOLUTION 1


# START: SOLUTION 2
def print_pattern_solution_2():
    for i in range(4):
        if i in (0, 3):
            print('*' * 5)
        else:
            print('*', '*', sep=' ' * 3)

# Executed 10000 time in 0.08560538291931152 second(s).
# END: SOLUTION 2


if __name__ == '__main__':
    print_pattern_solution_1()
    print_pattern_solution_2()
