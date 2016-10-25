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


def bounds(ls, pos):
	return int(pos) in range(len(ls))


def add(args):
	if len(args) != 1:
		invalid_syntax()
	validate(args[0])


def insert(ls, args):
	match = re.search(r"^(.+)at(\d+)$", "".join(args))

	if not match:
		invalid_syntax()

	pos = int(match.groups()[1])

	if pos < 0 or pos > len(ls):
		invalid_bounds()

	validate(match.group()[0])


def remove(ls, args):
	match = re.search(r"^(\d+)$", "".join(args))

	if match:
		if not bounds(ls, match.groups()[0]):
			invalid_bounds()
		return

	match = re.search(r"^(\d+)to(\d+)$", "".join(args))
	if not match:
		invalid_syntax()
	if not bounds(ls, match.groups()[0]) or not bounds(ls, match.groups()[1]):
		invalid_bounds()


def replace(ls, args):
	match = re.search(r"^(.+)with(.+)$", "".join(args))
	if not match:
		invalid_syntax()
	map(validate, match.groups())


def lists(ls, args):
	if len(args) == 0:
		return
	match = re.search(r"^real(\d+)to(\d+)$", "".join(args))
	if match:
		a, b = match.groups()
		if not bounds(ls, a) or not bounds(ls, b) or a > b:
			invalid_bounds()
		return
	
	match = re.search(r"^modulo[<=>]\d+$", "".join(args))
	if not match:
		invalid_syntax()

def sums(ls, args):
	match = re.search(r"^(\d+)to(\d+)$", "".join(args))
	a, b = match.groups()
	if not match:
		invalid_syntax()
	if not bounds(ls, a) or not bounds(ls, b) or a > b:
		invalid_bounds()


def product(ls, args):
	match = re.search(r"^(\d+)to(\d+)$", "".join(args))
	a, b = match.groups()
	if not match:
		invalid_syntax()
	if not bounds(ls, a) or not bounds(ls, b) or a > b:
		invalid_bounds()


def filter(ls, args):
	if len(args) == 1 and args[0] == "real":
		return
	match = re.search(r"^modulo[<=>]\d+$", "".join(args))
	if not match:
		invalid_syntax()

def undo(ls, args, undo_stack):
	if len(args) != 0:
		invalid_syntax()
	if len(undo_stack) == 0:
		raise Exception("I have nothing to undo")