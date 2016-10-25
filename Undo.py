# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

def create_undo_command(id_cmd, command, arg1, arg2):
	return {"id":id_cmd, "command":command, "arg1":arg1, "arg2":arg2}

def new_undo(undo_stack):
	return last_undo(undo_stack)+1
	return undo_stack

def push_undo(undo_stack, command):
	# print("cmd", command)
	undo_stack.append(command)

def pop_undo(undo_stack):
	undo_id = last_undo(undo_stack)
	for cmd in reversed(undo_stack):
		if cmd["id"] != undo_id:
			return undo_stack
		undo_stack.pop()
	return undo_stack

def last_undo(undo_stack):
	if len(undo_stack) == 0:
		return 0
	# print("lastundo", undo_stack[-1])
	return undo_stack[-1]["id"]

def run_undo(undo_stack, ls):
	undo_id = last_undo(undo_stack)

	for cmd in reversed(undo_stack):
		if cmd["id"] != undo_id:
			return undo_stack 
		cmd["command"](ls, cmd["arg1"], cmd["arg2"])
	return undo_stack