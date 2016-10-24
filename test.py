def funct():
	raise ValueError

try:
	funct()
	assert(Flase)
except Exception as e:
	assert(isinstance(e, ValueError))