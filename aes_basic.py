#!/usr/bin/env python3

from Crypto.Cipher import AES

print("\nAES basic encryption showcase\n\n")

key = b"0000111122223333"
cipher = AES.new(key, AES.MODE_ECB)
a = b"Hello from AES!!"
ciphertext = cipher.encrypt(a)
print("Ciphertext: " + ciphertext.hex())

cipher = AES.new(key, AES.MODE_ECB)
d = cipher.decrypt(ciphertext)
print("\nDecrypted message: " + d.decode("UTF-8") + "\n")
