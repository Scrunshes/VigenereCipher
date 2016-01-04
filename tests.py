from VigenereCipher import VigenereCipher


def simpleTest():
    vigenere = VigenereCipher()
    text_to_encrypt = "Ceci est/\. 1 t3xt à chiffrè   "
    key = "AHDSQHDQSD"

    text_encrypted = vigenere.encrypt(text_to_encrypt, key)

    text_decrypted = vigenere.decrypt(text_encrypted, key)

    assert(text_to_encrypt == text_decrypted), "Text to encrypt is not equal to decrypted text."
    assert(len(text_to_encrypt) == len(text_decrypted)), "Text to encrypt and decrypted text not of the same length."


simpleTest()
