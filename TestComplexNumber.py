# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import ComplexNumber
from ComplexNumber import create as cn
def run():
	validate()
	create()
	format()
	modulo()
	sum()
	multiply()

def create():
	assert(ComplexNumber.create("1+2j") == {"real":1, "imag":2})
	assert(ComplexNumber.create("3-2j") == {"real":3, "imag":-2})
	assert(ComplexNumber.create("-1+12j") == {"real":-1, "imag":12})

def validate():
	try:
		ComplexNumber.validate(1212)
		assert(False)
	except Exception as ex:
		assert(isinstance(ex, AttributeError))
	try:
		ComplexNumber.validate("1+2ji")
		assert(False)
	except Exception as ex:
		assert(isinstance(ex, ValueError))
	try:
		ComplexNumber.validate("2--i12")
		assert(False)
	except Exception as ex:
		assert(isinstance(ex, ValueError))


def format():
	assert(ComplexNumber.format(cn(1+2j)) == "1+2i")
	assert(ComplexNumber.format(cn(-10)) == "-10")
	assert(ComplexNumber.format(cn(2j)) == "2i")


def modulo():
	assert(ComplexNumber.modulo(cn(1)) == 1)
	assert(ComplexNumber.modulo(cn(2j)) == 2)
	assert(ComplexNumber.modulo(cn(3+4j)) == 5)


def sum():
	assert(ComplexNumber.add(cn(1), cn(2j)) == cn(1+2j))
	assert(ComplexNumber.add(cn(-1), cn(2j)) == cn(-1+2j))
	assert(ComplexNumber.add(cn(2j), cn(2j)) == cn(4j))


def multiply():
	assert(ComplexNumber.multiply(cn(-1j), cn(1j)) == cn(1))
	assert(ComplexNumber.multiply(cn(1j), cn(1j)) == cn(-1))
	assert(ComplexNumber.multiply(cn(2-1j), cn(3+1j)) == cn(7-1j))



	