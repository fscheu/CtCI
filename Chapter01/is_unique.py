''' is_unique.py '''
import string

def is_unique(a_string: string) -> bool:
    ''' Checks if the string has all different characters '''

    if len(a_string) > 128:
        return False

    # list_chars will hold a mark for each char
    list_chars = [False] * 128
    for _, letter in enumerate(a_string):
        if list_chars[ord(letter)]:
            #if its true is because the char is already present in the string
            return False
        else:
            list_chars[ord(letter)] = True

    return True
