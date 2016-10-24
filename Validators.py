# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import Commands
import HelpCommands
import re
from ComplexNumber import validate


def invalid_syntax():
    raise Exception("Invalid syntax!")


def invalid_bounds():
    raise Exception("Range out of bounds!")


def in_bounds(ls, pos):
    return int(pos) in range(len(ls))


def add(args):
    if len(args) != 1:
        invalid_syntax()
    validate(args[0])


def insert(ls, args):
    regex = r"^(.+)at(\d+)$"
    com = "".join(args)
    match = re.search(regex, com)

    if not match:
        invalid_syntax()

    pos = int(match.groups()[1])

    if pos < 0 or pos > len(ls):
        invalid_bounds()

    validate(match.group()[0])


def remove(ls, args):
    regex = r"^(\d+)$"
    com = "".join(args)
    match = re.search(regex, com)

    if match:
        if not in_bounds(ls, match.groups()[0]):
            invalid_bounds()
        return

    regex = r"^(\d+)to(\d+)$"
    match = re.search(regex, com)
    if not match:
        invalid_syntax()
    if not in_bounds(ls, match.groups()[0]) or not in_bounds(ls, match.groups()[1]):
        invalid_bounds()


def replace(ls, args):
    regex = r"^(.+)with(.+)$"
    com = "".join(args)
    match = re.search(regex, com)
    if not match:
        invalid_syntax()
    map(validate, match.groups())


def lists(ls, args):
    if len(args) == 0:
        return
    regex = r"^real(\d+)to(\d+)$"
    com = "".join(args)
    match = re.search(regex, com)
    if match:
        a, b = match.groups()
        if not in_bounds(ls, a) or not in_bounds(ls, b) or a > b:
            invalid_bounds()
        return
    
    regex = r"^modulo[<=>]\d+$"
    match = re.search(regex, com)
    if not match:
        invalid_syntax()

def sums(ls, args):
    regex = r"^(\d+)to(\d+)$"
    com = "".join(args)
    match = re.search(regex, com)
    a, b = match.groups()
    if not match:
        invalid_syntax()
    if not in_bounds(ls, a) or not in_bounds(ls, b) or a > b:
        invalid_bounds()


def product(ls, args):
    regex = r"^(\d+)to(\d+)$"
    com = "".join(args)
    match = re.search(regex, com)
    a, b = match.groups()
    if not match:
        invalid_syntax()
    if not in_bounds(ls, a) or not in_bounds(ls, b) or a > b:
        invalid_bounds()


def filter(ls, args):
    if len(args) == 1 and args[0] == "real":
        return
    com = "".join(args)
    regex = r"^modulo[<=>]\d+$"
    match = re.search(regex, com)
    if not match:
        invalid_syntax()    