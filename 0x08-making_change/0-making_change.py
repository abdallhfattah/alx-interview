#!/usr/bin/python3

"""make change"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of available coin denominations (positive int)
        total (int):  The target amount you want to achieve using the coins

    Returns:
        int : The minimum number of coins needed to meet the total.
        If it is not possible to meet the total, returns -1.
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return dp[-1] if dp[-1] != total + 1 else -1
