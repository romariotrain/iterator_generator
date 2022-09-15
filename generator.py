nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]


def gen(*args, **kwargs):
    for list_ in nested_list:
        for item in list_:
            yield item


for item in gen(nested_list):
    print(item)

flat_list = [item for item in gen(nested_list)]
print(flat_list)
