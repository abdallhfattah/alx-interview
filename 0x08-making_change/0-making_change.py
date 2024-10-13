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

    coins.sort()

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(total + 1):
        for coin in coins:
            if i - coin < 0:
                break
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
