from VigenereCipher import VigenereCipher

vigenere = VigenereCipher()

plain_text = "Ceci.../**/-534 est laqsdqsd544 phrase a chiffsQSrer     "
key = "qsdnqsdhqfsdklfjsdlf"

print(vigenere.encrypt(plain_text, key))


