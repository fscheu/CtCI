''' array_list.py'''
from tokenize import String


class ArrayList:
    ''' ArrayList class

        Keeps a list of fixed size and doubles it when needs more space'''
    def __init__(self, size=10) -> None:
        self._max_size = size
        self._list = [None] * size
        self._cur_pos = 0

    def add(self, a_string:String):
        ''' Adds a string to the array with each character in a different position'''
        while len(a_string) + self._cur_pos > self._max_size:
            self._increase_size()
        for _, a_char in enumerate(a_string):
            self._list[self._cur_pos] = a_char
            self._cur_pos += 1

    def _increase_size(self):
        self._list = self._list + [None] * self._max_size
        self._max_size *= 2

    def get(self, index=None):
        '''Gets the value of the index.
        If no index is provided returns a string with all the values'''

        if index is None:
            return ''.join(self._list[:(self._cur_pos)])

        if index >= self._cur_pos:
            raise Exception('Invalid index')

        return self._list[index]
