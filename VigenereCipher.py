import string


class VigenereCipher:

    @staticmethod
    def isascii(token):
        return token in string.ascii_letters

    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)

    def encrypt(self, plain_text, key):

        return self.act_on_text(self.decrypt_token, plain_text, key)

    def decrypt(self, cipher_text, key):

        return self.act_on_text(self.encrypt_token, cipher_text, key)

    def act_on_text(self, action, text, key):

        if len(key) > len(text):
            return "Your key must be less or equal to the length of the cipher text you want to decrypt."

        if not key.isalpha():
            return "Your key must just be composed of letters."

        if len(key) < 1 or len(text) < 1:
            return "Your key and the text must be at least of one character."

        key_count = 0
        key_length = len(key)
        final_text = []

        for token in text:
            if not self.isascii(token):
                final_text.append(token)
                key_count += 1
                continue

            if key_count >= key_length:
                key_count = 0

            final_text.append(self.act_on_token(action,token, key[key_count]))

            key_count += 1

        return ''.join(map(str, final_text))

    def encrypt_token(self, token_id, key_id):

        return self.alphabet[(token_id + key_id) % 26]

    def decrypt_token(self, token_id, key_id):

        return self.alphabet[(token_id - key_id) % 26]

    def act_on_token(self, action, token, key):

        is_token_upper = token.isupper()
        token_id = self.alphabet.index(token.lower())
        key_id = self.alphabet.index(key.lower())

        workable_token = action(token_id, key_id)

        if is_token_upper:
            return workable_token.upper()

        return workable_token
