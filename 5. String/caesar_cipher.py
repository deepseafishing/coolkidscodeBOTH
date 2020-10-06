#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.


def caesarCipher(s, k):
    new_s = ''
    for c in s:
        if c.islower():
            new_s += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        elif c.isupper():
            new_s += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            new_s += c

    return new_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
