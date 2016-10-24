import Commands
from ComplexNumber import create
from random import randint

def random_complex(realbound, imagbound):
	"""Creates a complex number with the real part in [-realbound, realbound] 
	and the imaginary part in [-imagbound, imagbound]
	
	Input data:
	realbound -- integer value representing the bounds of the real part
	imagbound -- integer value representing the bounds of the imag part
	Output data:
	The complex number generated 
	"""

	real = randint(-realbound, realbound)
	imag = randint(-imagbound, imagbound)
	real = str(real)
	imag = ("+" if imag >=0 else "") + str(imag)
	# print(real+imag+"i")
	return create(real+imag+"i")

def fake_fill(ls, args):
	"""Fills the given list with random complexes numbers
	
	Input data:
	ls -- the list to be filled
	args -- the list of parameters. All of them are optional
	args[0] -- the amount of numbers to be added. Defaults to 10
	args[1] -- the realbound. Defaults to 10
	args[2] -- the imagbound. Defaults to 10
	Output data:
	The filled list
	"""
	cnt = 10
	real = 10
	imag = 10
	if len(args) > 0:
		cnt = int(args[0])
	if len(args) > 1:
		real = int(args[1])
	if len(args) > 2:
		imag = int(args[2])

	for i in range(cnt):
		Commands.add(ls, random_complex(real, imag))
	return ls


def clear(ls, args):
	"""Clears the given list
	
	Input data:
	ls -- The list to be cleared
	args -- irrelevant. Leave empty
	Output data:
	Returns the empty list
	"""
	ls.clear()
	return ls