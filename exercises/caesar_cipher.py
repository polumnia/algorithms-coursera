class CaesarCipher:
    """Class for doing encryption and decryption using Caesar cipher"""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation"""
        alphabet_size = 26
        encoder = [None] * alphabet_size
        decoder = [None] * alphabet_size
        for i in range(alphabet_size):
            encoder[i] = chr((i + shift) % alphabet_size + ord("A"))
            decoder[i] = chr((i - shift) % alphabet_size + ord("A"))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, decoded_str):
        return self._transform(decoded_str, self._forward)

    def decrypt(self, encoded_str):
        return self._transform(encoded_str, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message: ", answer)
