#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        letter = str[i]
        tmp = ord(letter)
        if tmp >= 97 and tmp < 123:
            tmp -= 32
            letter = chr(tmp)
        else:
            continue
    print("{}".format(letter))
