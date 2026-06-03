from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


class DESAlgorithm:
    def __init__(self, key):
        self.key = key.encode('utf-8')

        if len(self.key) != 8:
            raise ValueError("DES key must be exactly 8 bytes long")

        self.cipher = DES.new(self.key, DES.MODE_ECB)

    def encrypt(self, plaintext):
        plaintext = plaintext.encode('utf-8')
        padded_text = pad(plaintext, DES.block_size)

        encrypted = self.cipher.encrypt(padded_text)

        return encrypted.hex()

    def decrypt(self, ciphertext_hex):
        ciphertext = bytes.fromhex(ciphertext_hex)

        decrypted = self.cipher.decrypt(ciphertext)

        return unpad(decrypted, DES.block_size).decode('utf-8')


if __name__ == "__main__":
    key = "12345678"

    des = DESAlgorithm(key)

    message = "Hello DES"

    encrypted = des.encrypt(message)
    print("Encrypted:", encrypted)

    decrypted = des.decrypt(encrypted)
    print("Decrypted:", decrypted)
