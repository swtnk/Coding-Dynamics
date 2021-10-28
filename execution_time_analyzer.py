# -*- coding: utf-8 -*-

__author__ = "Swetank Subham"
__credits__ = ["Swetank Subham"]
__license__ = "GPL"

__maintainer__ = "Swetank Subham"
__website__ = "https://swetanksubham.com/"

import os, sys, argparse
from importlib import import_module
from time import time

def block_print_statement():
    sys.stdout = open(os.devnull, 'w')

def enable_print_statement():
    sys.stdout = sys.__stdout__

parser = argparse.ArgumentParser(description='Average execution time analyzer using iterative approach.')
required_arguments = parser.add_argument_group('required arguments')
required_arguments.add_argument('-f', '--filename', type=str, help='File from which method needs to be executed', required=True)
required_arguments.add_argument('-m', '--method', type=str, help='Method which needs to be executed', required=True)
parser.add_argument('-i', '--iterations', type=int, help='Method which needs to be executed. [default=10]', default=10)

args = parser.parse_args()

module = import_module(args.filename)
method = getattr(module, args.method)
iterations = args.iterations

st = time()
ITERATIONS = int(iterations) if iterations else 10

block_print_statement()

for _ in range(ITERATIONS):
    method()

enable_print_statement()

print(f'Executed { ITERATIONS } time in { time() - st } second(s).')
