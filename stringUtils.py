import string
import unicodedata
import re


alphabet = list(string.ascii_lowercase)


def isascii(text):
    """
    Vérfifie que le(s) caractère(s) donné(s) apparatien(nen)t au standard ASCII.
    :param input (str): caractère(s) à vérfier.
    :return (boolean): état de la vérification.
    """

    if len(text) == 1:
        return text in string.ascii_letters

    for token in text:
        if not token in string.ascii_letters:
            return False

    return True


def normalize_text(raw_text):
    """
    Met en forme le texte de façon a ce qu'il soit utilisable pour l'indice de coincidence nottament.
    :param raw_text (str): texte brut
    :return: texte transformé où tout caractère non-ascii a été remplacé par son équivalent ou bien supprimé.
    """
    return unicodedata.normalize('NFKD', re.sub('\W+', '', raw_text)).encode('ascii', 'ignore').decode('ascii')

