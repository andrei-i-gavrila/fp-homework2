# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import Commands
from ComplexNumber import create as cn


def run():
	test_undo_insert()
	test_undo_remove()
	test_undo_add()
	test_undo_replace()
	test_undo_filter_real()
	test_undo_filter_modulo()


def test_undo_insert():
	ls = []
	undo_stack = []
	Commands.insert(ls, cn(1), 0, undo=undo_stack)
	assert(len(undo_stack) == 1)
	Commands.insert(ls, cn(2), 1, undo=undo_stack)
	assert(len(undo_stack) == 2)
	Commands.undo(ls, undo_stack)
	assert(len(undo_stack) == 1)
	assert(ls == [cn(1)])
	Commands.undo(ls, undo_stack)
	assert(ls == [])

def test_undo_remove():
	ls = []
	undo_stack = []
	Commands.add(ls, cn(1))
	Commands.add(ls, cn(2))
	Commands.add(ls, cn(3))
	assert(len(ls) == 3)
	assert(undo_stack == [])
	Commands.remove(ls, 0, 0, undo=undo_stack)
	assert(len(undo_stack) == 1)
	assert(ls == [cn(2), cn(3)])
	Commands.remove(ls, 0, 1, undo=undo_stack)
	assert(len(undo_stack) == 3)
	assert(ls == [])
	Commands.undo(ls, undo_stack)
	assert(ls == [cn(2), cn(3)])
	assert(len(undo_stack) == 1)
	Commands.undo(ls, undo_stack)
	assert(ls == [cn(1), cn(2), cn(3)])
	assert(len(undo_stack) == 0)

def test_undo_add():
	ls = []
	undo_stack = []
	Commands.add(ls, cn(1), undo=undo_stack)
	assert(len(undo_stack) == 1)
	Commands.undo(ls, undo_stack)
	assert(len(undo_stack) == 0)
	assert(ls == [])

def test_undo_replace():
	ls = []
	undo_stack = []
	Commands.add(ls, cn(2))
	Commands.add(ls, cn(3))
	Commands.add(ls, cn(2))
	assert(ls == [cn(2), cn(3), cn(2)])
	Commands.replace(ls, cn(2), cn(10), undo=undo_stack)
	assert(len(undo_stack) == 4)
	assert(ls == [cn(10), cn(3), cn(10)])
	Commands.undo(ls, undo_stack)
	assert(len(undo_stack) == 0)
	assert(ls == [cn(2), cn(3), cn(2)])


def test_undo_filter_real():
	ls = []
	undo_stack = []
	Commands.add(ls, cn(2))
	Commands.add(ls, cn(3))
	Commands.add(ls, cn(2j))
	Commands.add(ls, cn(1j))
	Commands.filter_real(ls, undo=undo_stack)
	assert(ls == [cn(2), cn(3)])
	assert(len(undo_stack) == 2)
	Commands.undo(ls, undo_stack)
	assert(ls == [cn(2), cn(3), cn(2j), cn(1j)])
	assert(len(undo_stack) == 0)


def test_undo_filter_modulo():
	ls = []
	undo_stack = []
	Commands.add(ls, cn(2))
	Commands.add(ls, cn(3))
	Commands.add(ls, cn(2j))
	Commands.add(ls, cn(1j))
	Commands.filter_modulo(ls, float.__lt__, 2.0, undo=undo_stack)
	assert(ls == [cn(1j)])
	assert(len(undo_stack) == 3)
	Commands.undo(ls, undo_stack)
	assert(ls == [cn(2), cn(3), cn(2j), cn(1j)])
	assert(len(undo_stack) == 0)