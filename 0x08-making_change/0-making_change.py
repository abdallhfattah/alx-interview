#!/usr/bin/python3

"""make change"""


def makeChange(coins, total):
    """
    make change (greedy solution probably will not work)
    """
    sorted(coins)
    if total <= 0:
        return 0
    number_of_coins = 0
    for coin in reversed(coins):
        if total % coin == 0:
            what_i_will_take = total // coin
            number_of_coins += number_of_coins
            total -= what_i_will_take * coin
    if total != 0:
        return -1
    else:
        return number_of_coins
