# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import Commands
import Validators
import ComplexNumber
import HelpCommands
import Helper

def cmds_list():
	return {
		"help": help,
		"add": add,
		"insert": insert,
		"remove": remove,
		"replace": replace,
		"list": lists,
		"sum": sums,
		"product": product,
		"filter": filter,
		"gen": Helper.fake_fill,
		"clear": Helper.clear,
		"undo": undo,
		"lsundo": listundo,
	}


def read_command():
	long_cmd = input(">> ").split()
	return (long_cmd[0].lower(), long_cmd[1:]) if len(long_cmd) != 0 else ("invalid", [])


def invalid(ls, args, **kwargs):
	raise Exception("Invalid command. You could use some help")


def get_cmd(command):
	cmds = cmds_list()
	return cmds[command] if command in cmds else invalid


def help(ls, args, **kwargs):
	print("#" * 80)
	for method in dir(HelpCommands):
		if method[0] != "_":
			print("=>" + method[1:] + ":", getattr(HelpCommands, method)(), "\n")
	print("#" * 80)


def listundo(ls, args, **kwargs):
	if len(kwargs["undo"]) == 0:
		print("No elements in the undo stack!")
	for undo in kwargs["undo"]:
		print(undo)


def add(ls, args, **kwargs):
	Validators.add(args)
	Commands.add(ls, ComplexNumber.create(args[0]), **kwargs)


def insert(ls, args, **kwargs):
	Validators.insert(ls, args)
	Commands.insert(ls, ComplexNumber.create(args[0]), int(args[2]), **kwargs)


def remove(ls, args, **kwargs):
	Validators.remove(ls, args)
	if len(args) == 1:
		Commands.remove(ls, int(args[0]), int(args[0]), **kwargs)
	else:
		Commands.remove(ls, int(args[0]), int(args[2]), **kwargs)


def replace(ls, args, **kwargs):
	Validators.replace(ls, args)
	old = ComplexNumber.create(args[0])
	new = ComplexNumber.create(args[2])
	Commands.replace(ls, old, new, **kwargs)


def lists(ls, args, **kwargs):
	Validators.lists(ls, args)
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
	Validators.undo(ls, args, kwargs["undo"])
	if len(args) != 0:
		raise Exception("Invalid syntax!")

	Commands.undo(ls, kwargs["undo"])
