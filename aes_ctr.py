#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from os import urandom
from struct import unpack

print("\nAES-CTR encryption showcase\n\n")

# Generate a random 16-byte key
k = urandom(16)

# Print the key in hexadecimal
print("Key = " + str((hexa(k)), "utf-8") + "\n")

# Pick a starting value for the counter
nonce = unpack("<Q", urandom(8))[0]
print("Nonce = " + str(nonce) + "\n")

# Instantiate a counter function
ctr = Counter.new(128, initial_value=nonce)

# Create an AES object in CTR mode, using ctr as the counter
aes = AES.new(k, AES.MODE_CTR, counter=ctr)

# Plaintext
p = b"\x00\x01\x02\x03\x04"

# Encrypt the plaintext
c = aes.encrypt(p)

# Print the ciphertext in hexadecimal
p_string = str((hexa(p)), "utf-8")
c_string = str((hexa(c)), "utf-8")
print("Encrypted " + p_string + " to " +c_string)

# Decrypt the ciphertext
aes = AES.new(k, AES.MODE_CTR, counter=ctr)
p = aes.encrypt(c)

# Print the decrypted plaintext in hexadecimal
p_string = str((hexa(p)), "utf-8")
c_string = str((hexa(c)), "utf-8")
print("Encrypted " + c_string + " to " + p_string + "\n")

