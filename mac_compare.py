#!/usr/bin/env python3

from time import time

MAC1 = '0123456789abcdef'
MAC2 = '01X3456789abcdef'

TRIALS = 100000

def compare_mac(x, y, n):
  for i in range(n):
    if x[i] != y[i]:
      return False
  return True


# each call to verify_mac() will look at all eight bytes
start = time()
for i in range(TRIALS):
  compare_mac(MAC1, MAC1, len(MAC1))
end = time()
print("%0.5f" % (end-start))

# each call to verify_mac() will look at three bytes
start = time()
for i in range(TRIALS):
  compare_mac(MAC1, MAC2, len(MAC1))
end = time()
print("%0.5f" % (end-start))
