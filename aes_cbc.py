#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii
from os import urandom
from textwrap import wrap

BLOCKLEN = 16
n = (16 * 2)

print("\nAES-CBC encryption showcase\n\nHow many blocks?")
x = input()

# generate a random 16-byte key
k = urandom(16)

# print the key
print("\nKey = " + str((binascii.hexlify(k)), "utf-8"))

# pick a random IV
iv = urandom(16)
print("\nIV = " + str((binascii.hexlify(iv)), "utf-8"))

# pick an instance of AES in CBC mode
cipher = Cipher(algorithms.AES(k), modes.CBC(iv), backend=default_backend())
aes = cipher.encryptor()

p = b"\x00" * BLOCKLEN * int(x)

c = aes.update(p) + aes.finalize()
p_string = str((binascii.hexlify(p)), "utf-8")
c_string = str((binascii.hexlify(c)), "utf-8")
print("\nEncrypted " + str(wrap(p_string, n)) + " to:")
print("          " + str(wrap(c_string, n)) + "\n")

# now with a different IV and the same key
print("\n\nSecond round:")
iv = urandom(16)
print("\nIV = " + str((binascii.hexlify(iv)), "utf-8"))

cipher = Cipher(algorithms.AES(k), modes.CBC(iv), backend=default_backend())
aes = cipher.encryptor()
c = aes.update(p) + aes.finalize()
p_string = str((binascii.hexlify(p)), "utf-8")
c_string = str((binascii.hexlify(c)), "utf-8")
print("\nEncrypted " + str(wrap(p_string, n)) + " to:")
print("          " + str(wrap(c_string, n)) + "\n")
