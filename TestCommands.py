# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import HelpCommands
import Commands
from ComplexNumber import create as cn

def run():
	insert()
	add()
	remove()
	replace()
	lists()
	list_modulo()
	list_real_range()
	sums()
	product()
	filter_real()
	filter_modulo()

def has_help(method):
	return method in (function[1:] for function in dir(HelpCommands))

def add():
	assert(Commands.add([], cn(2j)) == [cn(2j)])
	assert(Commands.add([cn(1 + 2j), cn(3j)], cn(-2j)) == [cn(1 + 2j), cn(3j), cn(-2j)])
	assert(Commands.add([cn(1 + 2j), cn(3j)], cn(2)) == [cn(1 + 2j), cn(3j), cn(2)])
	assert(Commands.add([cn(3)], cn(2)) == [cn(3), cn(2)])
	assert(has_help("add"))


def insert():
	assert(Commands.insert([], cn(1), 0) == [cn(1)])
	assert(Commands.insert([cn(1), cn(2), cn(3)], cn(5), 1) == [cn(1), cn(5), cn(2), cn(3)])
	assert(Commands.insert([cn(1), cn(2), cn(3)], cn(1), 2) == [cn(1), cn(2), cn(1), cn(3)])
	assert(Commands.insert([cn(1), cn(2), cn(3), cn(5)], cn(15), 2) == [cn(1), cn(2), cn(15), cn(3), cn(5)])
	assert(has_help("insert"))  


def remove():
	assert(Commands.remove([cn(1), cn(2), cn(3), cn(4)], 0, 3) == [])
	assert(Commands.remove([cn(1), cn(2), cn(3), cn(4)], 0, 2) == [cn(4)])
	assert(Commands.remove([cn(1), cn(2), cn(3), cn(4)], 0, 0) == [cn(2), cn(3), cn(4)])
	assert(Commands.remove([cn(1), cn(2), cn(4)], 1, 1) == [cn(1), cn(4)])
	assert(has_help("remove"))


def lists():
	assert(Commands.lists([]) == [])
	assert(Commands.lists([cn(1), cn(2), cn(3)]) == [cn(1), cn(2), cn(3)])
	assert(Commands.lists([cn(2), cn(5), cn(2), cn(2 + 1j)]) == [cn(2), cn(5), cn(2), cn(2 + 1j)])
	assert(Commands.lists([cn(3 + 5j), cn(3 - 5j), cn(4)]) == [cn(3 + 5j), cn(3 - 5j), cn(4)])
	assert(has_help("list"))


def sums():
	assert(Commands.sums([cn(1)], 0, 1) == cn(1))
	assert(Commands.sums([], 0, 0) == cn(0))
	assert(Commands.sums([cn(1), cn(2), cn(3)], 1, 1) == cn(2))
	assert(has_help("sum"))


def list_modulo():
	assert(Commands.list_modulo([cn(1), cn(2), cn(3), cn(4), cn(5)], float.__gt__, 2.0) == [cn(3), cn(4), cn(5)])
	assert(Commands.list_modulo([cn(1), cn(2), cn(3), cn(4), cn(5)], float.__lt__, 4.0) == [cn(1), cn(2), cn(3)])
	assert(Commands.list_modulo([cn(1), cn(2), cn(3), cn(4), cn(5)], float.__eq__, 2.0) == [cn(2)])
	assert(Commands.list_modulo([cn(1 + 1j), cn(4 + 3j), cn(5j)], float.__eq__, 5.0) == [cn(4 + 3j), cn(5j)])


def list_real_range():
	assert(Commands.list_real_range([cn(1), cn(2j), cn(3), cn(4), cn(5)], 0, 3) == [cn(1), cn(3), cn(4)])
	assert(Commands.list_real_range([cn(2j), cn(3j), cn(4j), cn(3 + 5j), cn(-6j)], 0, 4) == [])
	assert(Commands.list_real_range([cn(1), cn(2), cn(3), cn(4), cn(5)], 0, 4) == [cn(1), cn(2), cn(3), cn(4), cn(5)])
	assert(Commands.list_real_range([cn(1 + 1j), cn(3 + 4j), cn(2), cn(4 + 3j), cn(5j)], 1, 2) == [cn(2)])


def product():
	assert(Commands.product([cn(1j), cn(1j)], 0, 1) == cn(-1))
	assert(Commands.product([cn(0), cn(1), cn(1j), cn(2j)], 1, 3) == cn(-2))
	assert(Commands.product([cn(1 + 1j), cn(2 + 2j), cn(0), cn(1)], 1, 3) == cn(0))
	assert(Commands.product([cn(1 + 1j), cn(2 + 3j)], 0, 1) == cn(-1 + 5j))
	assert(has_help("product"))


def replace():
	assert(Commands.replace([cn(1), cn(2), cn(3)], cn(2), cn(10)) == [cn(1), cn(10), cn(3)])
	assert(Commands.replace([cn(1), cn(2), cn(2), cn(3), cn(2), cn(4)], cn(2), cn(5)) == [cn(1), cn(5), cn(5), cn(3), cn(5), cn(4)])
	assert(Commands.replace([cn(1), cn(2 + 3j), cn(3 + 2j)], cn(2 + 3j), cn(3 + 2j)) == [cn(1), cn(3 + 2j), cn(3 + 2j)])

def filter_real():
	assert(Commands.filter_real([cn(1), cn(2), cn(1+2j), cn(3+1j)]) == [cn(1), cn(2)])
	assert(Commands.filter_real([cn(1)]) == [cn(1)])
	assert(Commands.filter_real([cn(1+2j), cn(3+1j)]) == [])


def filter_modulo():
	assert(Commands.filter_modulo([cn(1), cn(2), cn(1+2j), cn(3+1j)], float.__eq__, 2.0) == [cn(2)])
	assert(Commands.filter_modulo([cn(1)], float.__lt__, 2.0) == [cn(1)])
	assert(Commands.filter_modulo([cn(1+2j), cn(3+1j)], float.__gt__, 3.0) == [cn(3+1j)])



