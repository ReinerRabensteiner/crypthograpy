#!/usr/bin/env python3
import hashlib

h = "a"

for i in range(50):
  h = hashlib.new('md5', h.encode()).hexdigest()
  print(h)
