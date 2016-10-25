# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import Commands
import Validators
import ComplexNumber
import HelpCommands


def help(ls, args, **kwargs):
    for method in dir(HelpCommands):
        if method[0] != "_":
            print("=>" + method + ":", getattr(HelpCommands, method)(), "\n")


def add(ls, args, **kwargs):
    Validators.add(args)
    ls = Commands.add(ls, ComplexNumber.create(args[0]), **kwargs)
    

def insert(ls, args, **kwargs):
    Validators.insert(ls, args)
    ls = Commands.insert(ls, ComplexNumber.create(args[0]), int(args[2]), **kwargs)


def remove(ls, args, **kwargs):
    Validators.remove(ls, args)
    if len(args) == 1:
        ls = Commands.remove(ls, int(args[0]), int(args[0]), **kwargs)
    else:
        ls = Commands.remove(ls, int(args[0]), int(args[2]), **kwargs)


def replace(ls, args, **kwargs):
    Validators.replace(ls, args)
    old = ComplexNumber.create(args[0])
    new = ComplexNumber.create(args[2])
    ls = Commands.replace(ls, old, new, **kwargs)


def lists(ls, args, **kwargs):
    Validators.lists(ls, args)
    show = []
    if len(args) == 0:
        show = Commands.lists(ls)
    if len(args) == 4:
        show = Commands.list_real_range(ls, int(args[1]), int(args[3]))
    if len(args) == 3:
        ops = {"=": float.__eq__, "<": float.__lt__, ">": float.__gt__}
        show = Commands.list_modulo(ls, ops[args[1]], float(args[2]))

    show = ", ".join([ComplexNumber.format(i) for i in show])
    print(show if show != "" else "No results")


def sums(ls, args, **kwargs):
    Validators.sums(ls, args)
    s = Commands.sums(ls, int(args[0]), int(args[2]))
    print(ComplexNumber.format(s))


def product(ls, args, **kwargs):
    Validators.product(ls, args)
    p = Commands.product(ls, int(args[0]), int(args[2]))
    print(ComplexNumber.format(p))


def filter(ls, args, **kwargs):
    Validators.filter(ls, args)
    if len(args) == 1:
        Commands.filter_real(ls, **kwargs)
    if len(args) == 3:
        ops = {"=": float.__eq__, "<": float.__lt__, ">": float.__gt__}
        Commands.filter_modulo(ls, ops[args[1]], float(args[2]), **kwargs)

def undo(ls, args, **kwargs):
    #move to validators
    if len(args) != 0:
        raise Exception("Invalid syntax!")

    Commands.undo(ls, kwargs["undo"])