# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import ComplexNumber

def add(ls, complex_number):
    """Adds a complex number to a given list

    Input data:
    ls -- List of complex numbers
    complex_number -- the complex_number to be added to the list
    Output data:
    The modified list
    """
    ls.append(complex_number)
    return ls


def insert(ls, complex_number, position):
    """Inserts a complex_number into a given list at a given position

    Input data:
    ls -- List of complex numbers
    complex_number -- the complex number to be inserted
    position -- the index at which the complex number will be inserted
    Output data:
    The modified list
    """
    ls.insert(position, complex_number)
    return ls


def remove(ls, start, end):
    """Removes all the elements between start and end

    Input data:
    ls -- The list to be removed from
    start -- The start position
    end -- The end position 
    Output data:
    The modified list 
    """
    for i in range(end - start + 1	):
        del ls[start]
    return ls


def replace(ls, old, new):
    """Replaces all the apparitions of old with new

    Input data:
    ls -- The list to be changed 
    old -- The element to be replaced
    new -- The element to be replaced with
    Output data:
    The modified list
    """
    return [new if x == old else x for x in ls]

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


def list_modulo(ls, operator, comparator):
    """Lists all the elements in the list which fit in the given condition

    Input data:
    ls -- The list
    operator -- function object to be used for the condition
    comparator -- integer to use for the condition
    Output data:
    The list of all the numbers that fit in the condition
    """
    return [num for num in ls if operator(float(ComplexNumber.modulo(num)), comparator)]
    

def sums(ls, start, end):
    """Sums up all the numbers in the given range of the list

    Input data:
    ls -- The list
    start -- The starting point of the range
    end -- The end point of the range 
    Output data:
    The sum of the numbers in the given range
    """
    s = ComplexNumber.create("0")
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
    prod = ComplexNumber.create("1")
    for i in ls[start:end + 1]:
        prod = ComplexNumber.multiply(prod, i)
    return prod


def filter_real(ls):
    """Filters out all the non-real numbers
    
    Input data:
    ls -- the list to be filtered
    Output data:
    The filtered list
    """
    ls[:] = [num for num in ls if num["imag"] == 0]
    return ls


def filter_modulo(ls, operator, comparator):
    """Filters out all numbers that dont fit in the given condition
    
    Input data:
    ls -- The list to be filtered 
    operator -- The function name to be used by the condition
    comparator -- The integer to be used for the condition
    Output data:
    The filtered list
    """
    ls[:] = [num for num in ls if operator(float(ComplexNumber.modulo(num)), comparator)]
    return ls


def undo(ls):
    pass

