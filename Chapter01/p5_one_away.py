''' p5_one_away.py
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away

The insert and remove a character are the same case but opposite.
The replace case is different from the two previous. The two strings should be of the same length
'''

def is_one_away(word1, word2) -> bool:
    ''' Checks if word1 and word2 are one edit(remove, replace, insert) away'''
    if len(word1) == len(word2):
        return is_replace_case(word1,word2)
    elif len(word1)+1 == len(word2):
        return is_insert_case(word1, word2)
    elif len(word2)+1 == len(word1):
        return is_insert_case(word2, word1)
    return False

def is_insert_case(word1, word2) -> bool:
    ''' Checks if word1 and word2 are one edit away removing one char.
        word2 should be longer than word1'''
    ix_1 = 0
    ix_2 = 0
    diff = 0
    while (ix_1 < len(word1)) and (ix_2 < len(word2)):
        if word1[ix_1] != word2[ix_2]:
            diff += 1
            if diff > 1:
                return False
            ix_2 +=1
        else:
            ix_1 += 1
            ix_2 += 1
    return True

def is_replace_case(word1, word2) -> bool:
    ''' Checks if word1 and word2 are one edit away replacing one char'''
    ix_1 = 0
    ix_2 = 0
    diff = 0
    while (ix_1 < len(word1)) and (ix_2 < len(word2)):
        if word1[ix_1] != word2[ix_2]:
            diff += 1
            if diff > 1:
                return False
        ix_1 += 1
        ix_2 += 1
    return True
