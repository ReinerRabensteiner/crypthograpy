#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii
from os import urandom
from textwrap import wrap

BLOCKLEN = 16
n = (16 * 2)

print("\nAES-ECB encryption showcase\n\nHow many blocks?")
x = input()

# generate a random 16-byte key
k = urandom(16)

# print the key
print("\nKey = " + str((binascii.hexlify(k)), "utf-8"))

# create an AES-128 cipher in ECB mode
cipher = Cipher(algorithms.AES(k), modes.ECB(), backend=default_backend())
aes_encryptor = cipher.encryptor()

# set the plaintext block p to the all-zero string
p = b"\x00" * BLOCKLEN * int(x)

# encrypt the plaintext to ciphertext
c = aes_encryptor.update(p) + aes_encryptor.finalize()

# print the encrypted and decrypted blocks
p_string = str((binascii.hexlify(p)), "utf-8")
c_string = str((binascii.hexlify(c)), "utf-8")
print("\nEncrypted " + str(wrap(p_string, n)) + " to:")
print("          " + str(wrap(c_string, n)) + "\n")
