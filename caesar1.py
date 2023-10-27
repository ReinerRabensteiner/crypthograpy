#!/usr/bin/python3

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = input("Plaintext: ")
shift = int(input("Shift: "))
ciphertext = ""

for c in plaintext:
  i = letters.find(c) + shift
  if i >= len(letters):
    i -= len(letters)
  ciphertext += letters[i]

print("Ciphertext: ", ciphertext)
