nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
flat_list = []
for i in nested_list:
    for b in i:
        flat_list.append(b)

print(flat_list)
