#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        letter = str[i]
        if ord(letter) >= 97 and ord(letter) < 123:
            ord(letter) -= 32
        else:
            continue
    return (letter)
