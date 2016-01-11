import string


alphabet = list(string.ascii_lowercase)


def isascii(token):
    return token in string.ascii_letters


def calculate_keys_of(length, text):

    keys = []

    for index in range(length):
        keys[index] = []

    for index in range(text):
        keys[index % length] = text[index]

    return keys
