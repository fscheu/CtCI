''' p4_palindrome.py '''

# What does it take to be able to write a set of characters the same way forwards and backwards?
# We need to have an even number of almost all characters,
# so that half can be on one side and half can be on the other side.
# At most one character (the middle character) can have an odd count.

from collections import Counter
import string


def is_permutation_palindrome(word) -> bool:
    ''' check if any permutation of word is a palindrome'''
    word = clean(word)
    hash_table = Counter(word)
    count_odd = 0
    for a_count in hash_table.values():
        if a_count % 2:
            count_odd += 1

    return count_odd <= 1

def is_palindrome_bit_vector(phrase):
    """checks if a string is a permutation of a palindrome"""
    r = 0
    for c in clean(phrase):
        val = ord(c)
        mask = 1 << val
        if r & mask:
            r &= ~mask
        else:
            r |= mask
    return (r - 1) & r == 0

def clean(word):
    ''' removes any non ascii chars and converts to lower'''
    return [c for c in word.lower() if c in string.ascii_lowercase]
