#!/usr/bin/python3

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = input("Plaintext: ").upper()
shift = int(input("Shift: "))
ciphertext = ""

for c in plaintext:
  if c != " ":
    i = letters.find(c) + shift
    if i >= len(letters):
      i -= len(letters)
    ciphertext += letters[i]
  else:
    ciphertext += " " 

print("Ciphertext: ", ciphertext)
