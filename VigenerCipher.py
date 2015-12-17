class VigenerCipher:
    def __init__(self):
        pass;

    def encrypt(plainText, key):

        # Checking for bad entries which would make things go wrong.
        if len(key) > len(plainText):
            return "Your key must be less or equal to the lenght of the plain text you want to encrypt."

        if len(key) < 1 or len(plainText) < 1:
            return "Your key and the plain text you want to encrypt must be at least of one character."

        l = 0  # Counter of letter advancement of the encryption.
        k = 0  # Counter of the key advancement, only usefull if key is less long than plain text.
        # breakPoint  =
        cypherText = []

        # Looping through the plain text.s
        for token in plainText:
            # first verify if the token is a letter.
            if token.isAlpha === False:
                continue;

            cypherText.append(encryptLetter(token));

            k = k + 1
            l = l + 1

    def decrypt(cipherText, key):
        pass;

    def encryptToken(token, key):
        return (token + key) % 26

    def decryptToken(token, key):
        return (token - key) % 26
