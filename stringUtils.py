import string


alphabet = list(string.ascii_lowercase)


def isascii(token):
    return token in string.ascii_letters


def calculate_keys_of(length, text):

    if length == 0:
        return None

    keys = []

    for index in range(text):

        if not keys[index]:
            keys[index % length] = []

        keys[index % length] = text[index]

    return keys
