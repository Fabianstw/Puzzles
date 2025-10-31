if __name__ == '__main__':
	groups = open("inp.txt").read().strip().split('\n\n')
	
	exprs = {}
	
	for line in groups[1].split('\n'):
		v1, op, v2, arrow, v3 = line.split(' ')
		exprs[v3] = (v1, op, v2)
	
	# corrections
	# {('qwf', 'cnk'), ('mps', 'z27'), ('z14', 'vhm'), ('msq', 'z39')}
	for v1, v2 in (('qwf', 'cnk'), ('mps', 'z27'), ('z14', 'vhm'), ('msq', 'z39')):
		exprs[v1], exprs[v2] = exprs[v2], exprs[v1]
	
	print(f'digraph G {{')
	for v3 in exprs:
		(v1, op, v2) = exprs[v3]
		print(f'{v1} -> {v1}_{op}_{v2};')
		print(f'{v2} -> {v1}_{op}_{v2};')
		print(f'{v1}_{op}_{v2} -> {v3};')
	print(f'}}')
	
	swaps = sorted(['qwf', 'cnk', 'mps', 'z27', 'z14', 'vhm', 'msq', 'z39'])
	print(f'{",".join(swaps)}')