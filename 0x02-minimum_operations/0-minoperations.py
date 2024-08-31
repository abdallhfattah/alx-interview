#!/usr/bin/python3
""" module provides a function that helps in finding the
    minimum number of operations
    to reach exactly n 'H' characters
  """


def minOperations(n):
    """Compute the minimum number of operations
    to reach exactly n 'H' characters."""
    memo = {}

    def dp(count, copied):
        if count == n:
            return 0
        if count > n:
            return float("inf")

        if (count, copied) in memo:
            return memo[(count, copied)]

        res = float("inf")

        res = min(1 + dp(count + copied, copied), 2 + dp(count + count, count))
        memo[(count, copied)] = res
        return res

    return 1 + dp(1, 1)
