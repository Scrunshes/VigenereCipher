import string


alphabet = list(string.ascii_lowercase)

def isascii(token):
    return token in string.ascii_letters


def calculateKeysOf(length, text):

    keys = []

    for index in range(length):
        keys[index] = []

    for index in range(text):
        if (index)
