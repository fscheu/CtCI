''' urlify.py '''

import string


def urlify(a_url: string) -> string:
    a_url = a_url.strip()
    list_url = list(a_url)
    result = ""
    for _, a_char in enumerate(list_url):
        if a_char == " ":
            result = result + "%20"
        else:
            result = result + a_char

    return result
