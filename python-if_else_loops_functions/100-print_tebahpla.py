#!/usr/bin/python3

for letter in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - letter) % 2 == 0:
        print("{:c}".format(letter), end="")
    else:
        print("{:c}".format(letter - 32), end="")
