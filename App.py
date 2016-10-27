# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import UI
# import traceback
import Helper

def run():
	ls, undo_stack = [], []
	Helper.fake_fill(ls, [])
	while True:
		cmd, args = UI.read_command()

		if cmd == "exit":
			return

		cmd = UI.get_cmd(cmd)

		try:
			cmd(ls, args, undo=undo_stack)
		except Exception as ex:
			# traceback.print_exc()
			print("##", ex)
