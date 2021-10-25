import os, sys, argparse
from importlib import import_module
from time import time

def block_print_statement():
    sys.stdout = open(os.devnull, 'w')

def enable_print_statement():
    sys.stdout = sys.__stdout__

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='File from which method needs to be executed')
parser.add_argument('-m', '--method', help='Method which needs to be executed')
parser.add_argument('-i', '--iterations', help='Method which needs to be executed', default=10)

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
