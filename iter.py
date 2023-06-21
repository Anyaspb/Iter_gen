# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков
# и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.max_iteration = len(list_of_list)
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_counter = 0
        self.item_counter = 0
        return self

    def __next__(self):

        if self.list_counter >= self.max_iteration:
            raise StopIteration
        my_list = self.list_of_list[self.list_counter]

        if self.item_counter >= len(my_list):
            self.list_counter += 1
            self.item_counter = 0
            return self.__next__()
        my_item = my_list[self.item_counter]
        self.item_counter += 1
        return my_item







def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


test_1()
