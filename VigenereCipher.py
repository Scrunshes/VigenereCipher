from stringUtils import *
import mathUtils


def cryptanalysis(text, max_length):
    original_text_ic = mathUtils.ic_compute(text)
    keys = []

    print(original_text_ic)

    for index in range(max_length):
        #keys[index] =

def encrypt(plain_text, key):

    return act_on_text(decrypt_token, plain_text, key)


def decrypt(cipher_text, key):

    return act_on_text(encrypt_token, cipher_text, key)


def act_on_text(action, text, key):

    if len(key) > len(text):
        return "Your key must be less or equal to the length of the cipher text you want to decrypt."

    if not key.isalpha():
        return "Your key must just be composed of letters."

    if len(key) < 1 or len(text) < 1:
        return "Your key and the text must be at least of one character."

    # key_count = 0
    key_length = len(key)
    final_text = []
    index = -1

    for token in text:
        index += 1
        if not isascii(token):
            final_text.append(token)
            continue

        final_text.append(act_on_token(action, token, key[index % key_length]))

    return ''.join(map(str, final_text))


def encrypt_token(token_id, key_id):

    return alphabet[(token_id + key_id) % 26]


def decrypt_token(token_id, key_id):

    return alphabet[(token_id - key_id) % 26]


def act_on_token(action, token, key):

    is_token_upper = token.isupper()
    token_id = alphabet.index(token.lower())
    key_id = alphabet.index(key.lower())

    workable_token = action(token_id, key_id)

    if is_token_upper:
        return workable_token.upper()

    return workable_token
