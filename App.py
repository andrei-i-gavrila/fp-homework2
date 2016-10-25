# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import UI
import traceback
import Helper

def cmds_list():
	return {
		"help": UI.help,
		"add": UI.add,
		"insert": UI.insert,
		"remove": UI.remove,
		"replace": UI.replace,
		"list": UI.lists,
		"sum": UI.sums,
		"product": UI.product,
		"filter": UI.filter,
		"gen": Helper.fake_fill,
		"clear": Helper.clear,
		"undo": UI.undo,
	}

def invalid(ls, args, **kwargs):
	raise Exception("Invalid command. You could use some help")


def get_cmd(command):
	cmds = cmds_list()
	return cmds[command] if command in cmds else invalid
	# if command in cmds:
	#     return cmds[command]
	# else:
	#     return invalid


def read_command():
	long_cmd = input(">> ").split()
	return (long_cmd[0].lower(), long_cmd[1:]) if len(long_cmd) != 0 else ("invalid", []) 


def run():
	ls, undo_stack = [], []
	Helper.fake_fill(ls, [])
	while True:
		cmd, args = read_command()

		if cmd == "exit":
			return

		cmd = get_cmd(cmd)

		try:
			cmd(ls, args, undo=undo_stack)
		except Exception as ex:
			traceback.print_exc()
			print("##", ex)
