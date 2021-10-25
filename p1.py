# -*- coding: utf-8 -*-

__author__ = "Swetank Subham"
__credits__ = ["Swetank Subham"]
__license__ = "GPL"

__maintainer__ = "Swetank Subham"
__website__ = "https://swetanksubham.com/"

""" PROBLEM: Print pattern
A
BC
DEF
GHIJ
.
.
... upto Z
"""

# SOLUTION 1
def get_break_point():
    next_break_point, incrementor = 0, 1
    while True:
        yield next_break_point
        incrementor += 1
        next_break_point += incrementor

def print_pattern():
    break_point_index = get_break_point()
    break_point = None
    for index, alphabet in enumerate([chr(ascii) for ascii in range(65, 91)]):
        if break_point is None:
            break_point = next(break_point_index)
        if index != break_point:
            end = ''
        else:
            end = '\n'
            break_point = next(break_point_index)
        print(alphabet, end=end)
    print()

print_pattern()
