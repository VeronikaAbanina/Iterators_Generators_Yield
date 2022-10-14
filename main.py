nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# 1

for list_ in nested_list:
    for i in list_:
        print(i)


class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_
        self.cursor = -1
        self.list_len = len(self.list_)

    def __iter__(self):
        self.cursor += 1
        self.next = 0
        return self

    def __next__(self):
        if self.next == len(self.list_[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.next += 1
        return self.list_[self.cursor][self.next - 1]


if __name__ == '__main__':
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


# 2

def flat_generator(nested_list):
    for i in nested_list:
        yield i

if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)