#!/usr/bin/python3

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Text: ")

count = [0]*26

for c in text:
  if c != " ":
    i = letters.find(c)
    count[i] += 1

for c in letters:
  i = letters.find(c)
  print(c, count[i])
