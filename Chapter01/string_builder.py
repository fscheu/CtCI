''' string_builder.py'''
from io import StringIO

class StringBuilder:
    ''' Allows concatenation of multiple strings'''
    _string = None

    def __init__(self):
        self._string = StringIO()

    def add(self, a_str):
        '''Adds a string at the end'''
        self._string.write(a_str)

    def toString(self):
        return self._string.getvalue()

    def __str__(self):
        return self.toString()
