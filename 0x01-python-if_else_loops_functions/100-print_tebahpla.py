#!/usr/bin/python3
for n in range(122, 96, -1):
    char = n
    if ni % 2 != 0:
        char = char - 32
    print("{:c}".format(char), end="")
