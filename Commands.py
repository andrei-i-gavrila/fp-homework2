# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import ComplexNumber
import Undo

def add(ls, complex_number, **kwargs):
	"""Adds a complex number to a given list

	Input data:
	ls -- List of complex numbers
	complex_number -- the complex_number to be added to the list
	Output data:
	The modified list
	"""
	if "undo" in kwargs:
		kwargs["undo_id"] = Undo.choose_undo_id(kwargs)

	return insert(ls, complex_number, len(ls), **kwargs)


def insert(ls, complex_number, position, **kwargs):
	"""Inserts a complex_number into a given list at a given position

	Input data:
	ls -- List of complex numbers
	complex_number -- the complex number to be inserted
	position -- the index at which the complex number will be inserted
	Output data:
	The modified list
	"""
	if "undo" in kwargs:
		undo_id = Undo.choose_undo_id(kwargs)
		revcmd = Undo.create_undo_command(undo_id, remove, position, position)
		Undo.push_undo(kwargs["undo"], revcmd)

	ls.insert(position, complex_number)
	return ls


def remove(ls, start, end, **kwargs):
	"""Removes all the elements between start and end

	Input data:
	ls -- The list to be removed from
	start -- The start position
	end -- The end position 
	Output data:
	The modified list 
	"""
	if "undo" in kwargs:
		undo_id = Undo.choose_undo_id(kwargs)
		for i in range(start, end+1):
			revcmd = Undo.create_undo_command(undo_id, insert, ls[i], i)
			Undo.push_undo(kwargs["undo"], revcmd)

	for i in range(end - start + 1	):
		del ls[start]
	return ls


def replace(ls, old, new, **kwargs):
	"""Replaces all the apparitions of old with new

	Input data:
	ls -- The list to be changed 
	old -- The element to be replaced
	new -- The element to be replaced with
	Output data:
	The modified list
	"""
	if "undo" in kwargs:
		kwargs["undo_id"] = Undo.choose_undo_id(kwargs)
	for i, x in enumerate(ls):
		if x == old:
			remove(ls, i, i, **kwargs)
			insert(ls, new, i, **kwargs)
	return ls

def lists(ls):
	"""Returns the list

	Input data:
	ls -- The list 
	Output data:
	Returns the list
	"""
	return ls


def list_real_range(ls, start, end):
	"""Lists all real elements in a given range

	Input data:
	ls -- The list
	start -- The start of the range
	end -- The end of the range 
	Output data:
	A list of all the real elements in the given range
	"""
	return [num for num in ls[start:end+1] if num["imag"] == 0]


def list_modulo(ls, op, comp):
	"""Lists all the elements in the list which fit in the given condition

	Input data:
	ls -- The list
	op -- function object to be used for the condition
	comp -- integer to use for the condition
	Output data:
	The list of all the numbers that fit in the condition
	"""
	return [n for n in ls if op(float(ComplexNumber.modulo(n)), comp)]
	

def sums(ls, start, end):
	"""Sums up all the numbers in the given range of the list

	Input data:
	ls -- The list
	start -- The starting point of the range
	end -- The end point of the range 
	Output data:
	The sum of the numbers in the given range
	"""
	s = ComplexNumber.create(0)
	for cn in ls[start:end + 1]:
		s = ComplexNumber.add(s, cn)
	return s


def product(ls, start, end):
	"""Multiplies all the numbers in the given range of the list

	Input data:
	ls -- The list
	start -- The starting point of the range
	end -- The end point of the range 
	Output data:
	The product of the numbers in the given range
	"""
	prod = ComplexNumber.create(1)
	for i in ls[start:end + 1]:
		prod = ComplexNumber.multiply(prod, i)
	return prod


def filter_real(ls, **kwargs):
	"""Filters out all the non-real numbers
	
	Input data:
	ls -- the list to be filtered
	Output data:
	The filtered list
	"""
	if "undo" in kwargs:
		kwargs["undo_id"] = Undo.choose_undo_id(kwargs)
	for i, x in reversed(list(enumerate(ls))):
		if x["imag"] != 0:
			remove(ls, i, i, **kwargs)
	return ls


def filter_modulo(ls, op, comp, **kwargs):
	"""Filters out all numbers that dont fit in the given condition
	
	Input data:
	ls -- The list to be filtered 
	op -- The function name to be used by the condition
	comp -- The integer to be used for the condition
	Output data:
	The filtered list
	"""
	if "undo" in kwargs:
		kwargs["undo_id"] = Undo.choose_undo_id(kwargs)

	for i, x in reversed(list(enumerate(ls))):
		if not op(float(ComplexNumber.modulo(x)), comp):
			remove(ls, i, i, **kwargs)
	return ls


def undo(ls, undo_stack):
	Undo.run_undo(undo_stack, ls)
	Undo.pop_undo(undo_stack)
	return ls, undo_stack   

