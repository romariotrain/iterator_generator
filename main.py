nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:
    def __iter__(self):
        return self

    def __init__(self, list_):
        self.list_ = list_
        self.cursor = 0
        self.cursor_index = -1

    def __next__(self):
        self.cursor_index += 1
        while self.cursor_index > len(self.list_[self.cursor]) - 1:
            self.cursor += 1
            self.cursor_index = 0
            if self.cursor > len(self.list_) - 1:
                raise StopIteration
        # print(self.list_[self.cursor][self.cursor_index])
        return self.list_[self.cursor][self.cursor_index]

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)




