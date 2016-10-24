# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

def validate(complex_number):
    """Validates a complex number. Accepted forms <a+bi>, <a> or <bi>.

    Input data:
    complex_number -- A string representation of a complex number.
    Throws:
    ValueError when the complex_number has a wrong format
    AttributeError when the given argument is not a string
    """
    modified_complex = complex_number.replace("i", "j")
    try:
        complex(modified_complex)
    except Exception as e:
        raise ValueError("Invalid complex number. Try <a+bi>, <a>, or <bi>")


def create(complex_number):
    """Creates a numerical value of complex type from given string

    Input data:
    complex_number -- A string representation of a complex number <a+bi>, <a> or <bi>  
    Output data:
    A complex number created from the given string 
    """
    modified_complex = str(complex_number).replace("i", "j")

    compl = complex(modified_complex)
    return {"real": compl.real, "imag":compl.imag}


def format(complex_number):
    """Formats a complex number into a user-friendly format

    Input data:
    complex_number -- The complex number to be formatted	
    Output data:
    A string containing the complex number in a user friendly format
    """
    if complex_number["imag"] == 0:
        return str(int(complex_number["real"]))
    if complex_number["real"] == 0:
        return str(int(complex_number["imag"])) + "i"

    real = str(int(complex_number["real"]))
    imag = ("+" if complex_number["imag"] >= 0 else "") + str(int(complex_number["imag"]))
    return real+imag+"i"

def modulo(complex_number):
    """Returns the absolute value of the complex number
    
    Input data:
    complex_number -- The complex number for which we calculate the modulo 
    Output data:
    The absolute value of the complex number 
    """
    return float(complex_number["imag"]*complex_number["imag"] + complex_number["real"]*complex_number["real"])**0.5

def add(cn1, cn2):
    """Adds 2 complex numbers
    
    Input data:
    cn1 -- A complex number 
    cn2 -- A complex number
    Output data:
    A complex number which is equal to the sum of the 2 given
    """
    r = create(0+0j)
    r["real"] = cn1["real"] + cn2["real"]
    r["imag"] = cn1["imag"] + cn2["imag"]
    return r


def multiply(cn1, cn2):
    """Multiplies 2 complex numbers
    
    Input data:
    cn1 -- A complex number 
    cn2 -- A complex number
    Output data:
    A complex number which is equal to the product of the 2 given
    """

    r = create(0+0j)
    r = add(r, {"real":-(cn1["imag"]*cn2["imag"]) + cn1["real"]*cn2["real"], "imag":0})
    r = add(r, {"imag": (cn1["imag"]*cn2["real"]) + (cn1["real"]*cn2["imag"]), "real":0})
    return r
