# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import Commands
import HelpCommands
import ComplexNumber
import Helper
from ComplexNumber import create as cn

def has_help(method):
    return method in dir(HelpCommands)


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
    assert(has_help("lists"))


def sums():
    assert(Commands.sums([cn(1)], 0, 1) == cn(1))
    assert(Commands.sums([], 0, 0) == cn(0))
    assert(Commands.sums([cn(1), cn(2), cn(3)], 1, 1) == cn(2))
    assert(has_help("sums"))


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


def CN_create():
    assert(ComplexNumber.create("1+2j") == {"real":1, "imag":2})
    assert(ComplexNumber.create("3-2j") == {"real":3, "imag":-2})
    assert(ComplexNumber.create("-1+12j") == {"real":-1, "imag":12})


def CN_validate():
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


def CN_format():
    assert(ComplexNumber.format(cn(1+2j)) == "1+2i")
    assert(ComplexNumber.format(cn(-10)) == "-10")
    assert(ComplexNumber.format(cn(2j)) == "2i")


def CN_modulo():
    assert(ComplexNumber.modulo(cn(1)) == 1)
    assert(ComplexNumber.modulo(cn(2j)) == 2)
    assert(ComplexNumber.modulo(cn(3+4j)) == 5)


def CN_sum():
    assert(ComplexNumber.add(cn(1), cn(2j)) == cn(1+2j))
    assert(ComplexNumber.add(cn(-1), cn(2j)) == cn(-1+2j))
    assert(ComplexNumber.add(cn(2j), cn(2j)) == cn(4j))


def CN_multiply():
    assert(ComplexNumber.multiply(cn(-1j), cn(1j)) == cn(1))
    assert(ComplexNumber.multiply(cn(1j), cn(1j)) == cn(-1))
    assert(ComplexNumber.multiply(cn(2-1j), cn(3+1j)) == cn(7-1j))


def HELP_random_complex():
    num = Helper.random_complex(10, 10)
    assert(num["real"] <= 10 and num["real"] >= -10 and num["imag"] <= 10 and num["imag"] >= -10)
    num = Helper.random_complex(64, 10)
    assert(num["real"] <= 64 and num["real"] >= -64 and num["imag"] <= 10 and num["imag"] >= -10)
    num = Helper.random_complex(10, 0)
    assert(num["real"] <= 10 and num["real"] >= -10 and num["imag"] == 0)


def HELP_fake_fill():
    ls = []
    Helper.fake_fill(ls, [])
    assert(len(ls) == 10)
    ls = []
    Helper.fake_fill(ls, ["12"])
    assert(len(ls) == 12)
    ls = []
    Helper.fake_fill(ls, ["100", "20", "30"])
    assert(len(ls) == 100)
    for c in ls:
        assert(c["real"] <= 20 and c["real"] >= -20 and c["imag"] <= 30 and c["imag"] >= -30)

def HELP_clear():
    ls = []
    Helper.fake_fill(ls, [])
    Helper.clear(ls, [])
    assert(len(ls) == 0)

def run():  
    add()
    insert()
    remove()
    lists()
    sums()
    list_modulo()
    list_real_range()
    product()
    replace()
    filter_real()
    filter_modulo()
    CN_create()
    CN_validate()
    CN_format()
    CN_modulo()
    CN_sum()
    CN_multiply()
    HELP_random_complex()
    HELP_fake_fill()
    HELP_clear()
