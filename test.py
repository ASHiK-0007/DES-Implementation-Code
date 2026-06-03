from des import DESAlgorithm

key = "12345678"

des = DESAlgorithm(key)

plaintext = "Cyber Security Lab"

encrypted = des.encrypt(plaintext)

decrypted = des.decrypt(encrypted)

print("Original :", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
