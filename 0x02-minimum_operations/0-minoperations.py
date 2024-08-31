#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """Minimum Operations needed to get n H characters"""
    next = 1
    body = 1
    op = 0
    while body < n:
        if n % body == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if body != n:
        return 0
    return op
