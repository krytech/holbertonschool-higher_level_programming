#!/usr/bin/python3
for n in range(0, 8):
    for i in range(n + 1, 10):
        print("{:d}{:d}, ".format(n, i), end="")
print("{:d}{:d}".format(n + 1, i))
