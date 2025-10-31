from random import random

N = {'7': (0, 0),
     '8': (1, 0),
     '9': (2, 0),
     '4': (0, 1),
     '5': (1, 1),
     '6': (2, 1),
     '1': (0, 2),
     '2': (1, 2),
     '3': (2, 2),
     ' ': (0, 3),
     '0': (1, 3),
     'A': (2, 3)}

R = {' ': (0, 0),
     '^': (1, 0),
     'A': (2, 0),
     '<': (0, 1),
     'v': (1, 1),
     '>': (2, 1)}


path_dp = {}
length_dp = {}


def path(start, end):
	if (start, end) in path_dp:
		return path_dp[(start, end)]
	pad = N if (start in N and end in N) else R
	dx, dy = pad[end][0] - pad[start][0], pad[end][1] - pad[start][1]
	yy = ("^"*-dy) + ("v"*dy) # -2 * "v" = ""
	xx = ("<"*-dx) + (">"*dx)
	
	# move horizontal first, to be inside the pad
	if (pad[start][0], pad[start][1] + dy) == pad[" "]:
		return xx + yy + "A"
	# move vertical first, to be inside the pad
	if (pad[start][0] + dx, pad[start][1]) == pad[" "]:
		return yy + xx + "A"
	tmp = (xx+yy if random() < 0.5 else yy+xx) + "A"
	path_dp[(start, end)] = tmp
	return tmp

"""
Simulate letter by letter, for depth and then go to the next code
"""
def length(code, depth, s=0):
	if (code, depth) in length_dp:
		return length_dp[(code, depth)]
	if depth == 0: return len(code)
	for i in range(len(code)):
		s += length(path(code[i-1], code[i]), depth-1)
	length_dp[(code, depth)] = s
	return s

def solve(code, max_depth):
	path_dp.clear()
	length_dp.clear()
	return length(code, max_depth)

def simulate(code, max_depth):
	return min(solve(code, max_depth) for _ in range(200)) # take the min of 200 simulations

codes = open("inp.txt").read().split()
print("Part 1: " + str(sum(simulate(code, 3) * int(code[:-1]) for code in codes)))
print("Part 2: " + str(sum(simulate(code, 26) * int(code[:-1]) for code in codes)))