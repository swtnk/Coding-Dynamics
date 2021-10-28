# -*- coding: utf-8 -*-

__author__ = "Swetank Subham"
__credits__ = ["Swetank Subham"]
__license__ = "GPL"

__maintainer__ = "Swetank Subham"
__website__ = "https://swetanksubham.com/"

"""
PROBLEM: Print below mentioned pattern:
A
BC
DEF
GHIJ
.
.
... upto Z
"""

# START: SOLUTION 1
def get_break_point():
    next_break_point, incrementor = 0, 1
    while True:
        yield next_break_point
        incrementor += 1
        next_break_point += incrementor

def print_pattern_solution_1():
    break_point_index = get_break_point()
    break_point = None
    for index, alphabet in enumerate([chr(ascii_value) for ascii_value in range(65, 91)]):
        if break_point is None:
            break_point = next(break_point_index)
        if index != break_point:
            end = ''
        else:
            end = '\n'
            break_point = next(break_point_index)
        print(alphabet, end=end)
    print()

# Executed 100000 time in 2.9073073863983154 second(s).
# END: SOLUTION 1


# START: SOLUTION 2
def print_pattern_solution_2():
    ascii_value = 65
    for i in range(7):
        for j in range(i+1):
            alphabet = chr(ascii_value)
            print(alphabet, end='')
            ascii_value += 1
            if ascii_value > 90:
                break
        print()

# Executed 100000 time in 3.07146954536438 second(s).
# END: SOLUTION 2


if __name__ == '__main__':
    print_pattern_solution_1()
    print_pattern_solution_2()