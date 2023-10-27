#!/usr/bin/python3

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ciphertext = input("Ciphertext: ")

for shift in range(len(letters)):
  plaintext = ""
  for c in ciphertext:
    i = letters.find(c) + shift
    if i >= len(letters):
      i -= len(letters)
    plaintext += letters[i]
  print(shift, plaintext)
