# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

def create_undo_command(id_cmd, command, arg1, arg2):
	"""Creates an undo operation with 
	the command function, passing arg1 and arg2.
	Assigns it to the id_cmd batch
	
	Input data:
	id_cmd -- The id of the undo batch it belongs to. For grouping purposes
	command -- Function name for the undo command
	arg1 -- The first argument to pass to the function
	arg2 -- The second argument to pass to the function
	Output data:
	Dictionary containing id, command, arg1 and arg2
	"""
	return {"id":id_cmd, "command":command, "arg1":arg1, "arg2":arg2}

def get_id_undo(undo_stack):
	"""Gets an id for an undo batch
	
	Input data:
	undo_stack -- The undo stack to give the id from	
	Output data:
	Integer id representing the id of the undo batch
	"""
	return last_undo(undo_stack)+1


def push_undo(undo_stack, command):
	"""Pushes an undo command into the batch of undo
	
	Input data:
	undo_stack -- The undo stack to push into 
	command -- The command generated with create_undo_command
	Output data:
	The modified undo_stack 	Throws:
	"""
	undo_stack.append(command)
	return undo_stack


def pop_undo(undo_stack):
	"""Pops all the undo commands with the id from the latest batch
	
	Input data:
	undo_stack -- The undo stack to pop from 
	Output data:
	The modified undo_stack 
	"""
	undo_id = last_undo(undo_stack)
	for cmd in reversed(undo_stack):
		if cmd["id"] != undo_id:
			return undo_stack
		undo_stack.pop()
	return undo_stack


def last_undo(undo_stack):
	"""Returns the latest id from the stack given
	
	Input data:
	undo_stack -- The undo_stack to get the id from 
	Output data:
	The latest id from the undo_stack, 0 if there are none
	"""
	if len(undo_stack) == 0:
		return 0
	return undo_stack[-1]["id"]


def run_undo(undo_stack, ls):
	"""Runs the commands from the latest batch
	
	Input data:
	undo_stack -- The undo stack to be ran
	ls -- The list on which the operations will be ran
	Output data:
	Returns the list and the undo_stack modified
	"""
	undo_id = last_undo(undo_stack)
	for cmd in reversed(undo_stack):
		if cmd["id"] != undo_id:
			return ls, undo_stack 
		cmd["command"](ls, cmd["arg1"], cmd["arg2"])
	return ls, undo_stack


def choose_undo_id(kw):
	"""Choose an undo_id based on the kw.
	If "undo_id" is present in kw get that one
	Else create a new one
	
	Input data:
	kw -- the dictionary to check for undo_id
	Output data:
	The undo_id
	"""
	return kw["undo_id"] if "undo_id" in kw else get_id_undo(kw["undo"])
