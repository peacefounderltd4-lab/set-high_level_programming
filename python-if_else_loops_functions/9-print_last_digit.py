#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        char = i - 32
    else:
        char = i
    print("{}".format(chr(char)), end="")
