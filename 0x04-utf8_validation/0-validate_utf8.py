#!/usr/bin/python3

""" module to validate utf-8"""


def validUTF8(data) -> bool:
    for element in data:
        if element >= 256:
            return False

    return True
