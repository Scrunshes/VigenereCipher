import VigenereCipher


def simpletest():
    text_to_encrypt = "Ceci est/\. 1 t3xt à chiffrè   "
    key = "AHDSQHDQSD"

    text_encrypted = VigenereCipher.encrypt(text_to_encrypt, key)

    text_decrypted = VigenereCipher.decrypt(text_encrypted, key)

    assert(text_to_encrypt == text_decrypted), "Text to encrypt is not equal to decrypted text."
    assert(len(text_to_encrypt) == len(text_decrypted)), "Text to encrypt and decrypted text not of the same length."


def crypttest():
    print(VigenereCipher.cryptanalysis("Test"))

simpletest()
crypttest()
