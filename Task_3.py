class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list_index = 0
        self.current_item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list_index >= len(self.list_of_list):
            [].append([value if type(value) != list else FlatIterator(value) for value in self.list_of_list])
            raise StopIteration

        current_list = self.list_of_list[self.current_list_index]
        item = current_list[self.current_item_index]

        self.current_item_index += 1
        

        if self.current_item_index >= len(current_list):
            self.current_list_index += 1
            self.current_item_index = 0

        
        if type(item) == list and len(item) == 1:
            for item in FlatIterator(item):
                return item
        elif type(item) == list and len(item) > 1:
            self.list_of_list.append(item[-1])
            for index in FlatIterator(item):
                return index
        else:
            return item
list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

print([item for item in FlatIterator(list_of_lists_2)])
# def test_3():

#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]

#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):

#         assert flat_iterator_item == check_item

#     assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


# if __name__ == '__main__':
#     test_3()


