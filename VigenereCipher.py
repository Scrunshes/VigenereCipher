import stringUtils
from stringUtils import alphabet
import mathUtils


def compute_ic_of_keys(text, max_length):

    if max_length == 0:
        return None

    keys_ic = []

    for length in range(max_length):

        for index in range(len(text)):

            if not index % length in keys_ic:
                keys_ic.append([])

            keys_ic[index % length].append(text[index])

        return keys_ic


def cryptanalysis(raw_text, max_length):
    text = stringUtils.normalize_text(raw_text)
    original_text_ic = mathUtils.ic_compute(text)

    print(original_text_ic)

    print(compute_ic_of_keys(text, max_length))

    #for index in range(max_length):
        #keys[index] =


def encrypt(plain_text, key):
    """
    Appelle la fonction act_on_text avec comme action le chiffrement du texte.
    :param plain_text (str): le texte clair.
    :param key: la clé.
    :return (str): le texte chiffré.
    """
    return act_on_text(encrypt_token, plain_text, key)


def decrypt(cipher_text, key):
    """
    Appelle la fonction act_on_text avec comme action le déchiffrement du texte.
    :param cipher_text (str): le texte chiffré.
    :param key (str): la clé.
    :return: le texte déchiffré.
    """
    return act_on_text(decrypt_token, cipher_text, key)


def act_on_text(action, text, key):
    """
    Effectue une action sur le texte.
    :param action(function): l'action à éxécuter sur le texte.
    :param text (str): le texte sur lequel la fonction travaille.
    :param key (str): la clé utiliséé.
    :return: Le texte sur lequel l'action à été effectué.
    """

    """ Vérifie que la longueur de la clé n'est pas supérieur à la longueur du texte. """
    if len(key) > len(text):
        return "Your key must be less or equal to the length of the cipher text you want to decrypt."

    """ Vérifie que la clé est seulement composé de lettre ASCII. """
    if not stringUtils.isascii(key):
        return "Your key must just be composed of letters."

    """ Vérifie que la clé et le texte sont d'au moins un caractère. """
    if len(key) < 1 or len(text) < 1:
        return "Your key and the text must be at least of one character."

    key_length = len(key)
    final_text = []
    index = -1

    for token in text:
        index += 1
        if not stringUtils.isascii(token):
            final_text.append(token)
            continue
        print(action)
        final_text.append(act_on_token(action, token, key[index % key_length]))

    return ''.join(map(str, final_text))


def encrypt_token(token_id, key_id):
    """
    Chiffre la lettre donnée.
    :param token_id (int): la lettre sous forme numérique a chiffré.
    :param key_id (int):  la lettre de la clé correspondant sous forme numérique.
    :return: La lettre chiffrée sous forme numérique.
    """

    return alphabet[(token_id + key_id) % 26]


def decrypt_token(token_id, key_id):
    """
    Déchiffre la lettre donnée.
    :param token_id(int): la lettre sous forme numérique a déchiffré.
    :param key_id(int): la lettre de la clé correspondant sous forme numérique.
    :return: La lettre déchiffrée sous forme numérique.
    """

    return alphabet[(token_id - key_id) % 26]


def act_on_token(action, token, key):
    """
    Agit sur une lettre.
    :param action (function): action a effectué sur la lettre.
    :param token (str): lettre sur laquelle agir.
    :param key (str): lettre de la clé correspondant a l'avancement de l'action sur le texte.
    :return: une lettre utilisable dans le cadre de l'action en cours.
    """

    is_token_upper = token.isupper()
    token_id = alphabet.index(token.lower())
    key_id = alphabet.index(key.lower())

    workable_token = action(token_id, key_id)

    if is_token_upper:
        return workable_token.upper()

    return workable_token
