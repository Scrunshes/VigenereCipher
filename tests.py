import VigenereCipher


def simpletest():
    text_to_encrypt = "CECI est/\. 1 t3xt à chiffrè   "
    key = "DQDQSDKQSJDUAHDSQHDQSD"

    text_encrypted = VigenereCipher.encrypt(text_to_encrypt, key)

    text_decrypted = VigenereCipher.decrypt(text_encrypted, key)

    assert(text_to_encrypt == text_decrypted), "Text to encrypt is not equal to decrypted text."
    assert(len(text_to_encrypt) == len(text_decrypted)), "Text to encrypt and decrypted text not of the same length."

    print(text_encrypted)
    print(text_decrypted)


def crypttest():
    print(VigenereCipher.cryptanalysis("Test", 7))

simpletest()
# crypttest()
