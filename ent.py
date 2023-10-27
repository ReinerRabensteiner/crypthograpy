#!/usr/bin/python3

import math

prob = [.1, .9]
print("Probabilities:", prob)

e = 0.0
for p in prob:
  e -= p * math.log(p, 2)

print("Entropy:", e)
