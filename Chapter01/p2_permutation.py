''' Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other. '''

import string


def permutation(one_string: string, two_string: string) -> bool:
    '''Checks if one_string is a permutation of two_string'''
    if len(one_string) != len(two_string):
        return False

    dictionary = {}
    for _, a_char in enumerate(one_string):
        if a_char in dictionary.keys():
            dictionary[a_char] += 1
        else:
            dictionary[a_char] = 0

    for _, a_char in enumerate(two_string):
        if a_char in dictionary.keys():
            if dictionary[a_char] >= 1:
                dictionary[a_char] -= 1
            else:
                dictionary.pop(a_char)
        else:
            return False

    if len(dictionary) == 0:
        return True
    else:
        return False
