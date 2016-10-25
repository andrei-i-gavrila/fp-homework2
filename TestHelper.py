# Author: Gavrila Andrei
# Scope: Fundamentals of Programming homework

import Helper

def random_complex():
	num = Helper.random_complex(10, 10)
	assert(num["real"] <= 10 and num["real"] >= -10 and num["imag"] <= 10 and num["imag"] >= -10)
	num = Helper.random_complex(64, 10)
	assert(num["real"] <= 64 and num["real"] >= -64 and num["imag"] <= 10 and num["imag"] >= -10)
	num = Helper.random_complex(10, 0)
	assert(num["real"] <= 10 and num["real"] >= -10 and num["imag"] == 0)


def fake_fill():
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

def clear():
	ls = []
	Helper.fake_fill(ls, [])
	Helper.clear(ls, [])
	assert(len(ls) == 0)

def run():
	random_complex()
	fake_fill()
	clear()