''' p6_string_compression.py '''


def string_compression(phrase):
    ''' compress a string changing succession of letters with a count'''
    if phrase == "":
        return phrase

    res = ""
    count_char = 1
    for i_x in range(1,len(phrase)):
        if phrase[i_x] == phrase[i_x-1]:
            count_char += 1
        else:
            res = res + phrase[i_x-1] + str(count_char)
            count_char = 1

    #add the last char evaluated, could be a series or not
    res = res + phrase[-1] + str(count_char)

    if len(res) >= len(phrase):
        return phrase
    return res
