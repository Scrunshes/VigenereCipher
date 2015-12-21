import string


class VigenereCipher:

    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)

    def encrypt(self, plain_text, key):

        # Checking for bad entries which would make things go wrong.
        if len(key) > len(plain_text):
            return "Your key must be less or equal to the length of the plain text you want to encrypt."

        if len(key) < 1 or len(plain_text) < 1:
            return "Your key and the plain text you want to encrypt must be at least of one character."

        key_count = 0
        key_length = len(key)
        cipher_text = []

        # Looping through the plain text.
        for token in plain_text:
            # First verify if the token is a letter.
            if not token.isalpha():
                cipher_text.append(token)
                key_count += 1
                continue

            # Verify we are not going to go further in the string.
            if key_count >= key_length:
                key_count = 0

            cipher_text.append(self.encrypt_token(token, key[key_count]))

            key_count += 1

        return ''.join(map(str, cipher_text))

    def decrypt(self, cipher_text, key):

        if len(key) > len(cipher_text):
            return "Your key must be less or equal to the length of the cipher text you want to decrypt."

        if len(key) < 1 or len(cipher_text) < 1:
            return "Your key and the cipher text you want to encrypt must be at least of one character."

        key_count = 0
        key_length = len(key)
        plain_text = []

        for token in cipher_text:
            print(token)
            if not token.isAlpha():
                print("Not alpha")
                cipher_text.append(token)
                key_count += 1
                continue

            if key_count >= key_length:
                key_count = 0

            plain_text.append(self.decrypt_token(token, key[key_count]))

            key_count += 1

        return ', '.join(map(str, plain_text))

    def encrypt_token(self, token, key):

        isupper = token.isupper()              # Check if it's uppercase

        # We get corresponding id and don't forget to make char given lowercase.
        #print(token)
        token_id = self.alphabet.index(token.lower())
        key_id = self.alphabet.index(key.lower())

        encrypted_cipher = self.alphabet[(token_id + key_id) % 26]

        if isupper:
            return encrypted_cipher.upper()

        return encrypted_cipher

    def decrypt_token(self, token, key):
        return (token - key) % 26
