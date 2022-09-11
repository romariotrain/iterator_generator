nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]


def my_next(some_list):
    cursor = 0
    cursor_index = -1
    while True:
        cursor_index += 1
        while cursor_index > len(some_list[cursor]) - 1:
            cursor +=1
            cursor_index = 0
            if cursor > len(some_list) - 1:
                return
        yield some_list[cursor][cursor_index]

flat_list = [i for i in my_next(nested_list)]
print(flat_list)

