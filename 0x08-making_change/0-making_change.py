#!/usr/bin/python3

"""make change"""


def makeChange(coins, total):
    """
    make change (greedy solution probably will not work)
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    print(coins)
    number_of_coins = 0
    for coin in coins:
        if total == 0:
            break
        what_i_will_take = total // coin
        number_of_coins += what_i_will_take
        print(f"what i will take for the {coin} will be {what_i_will_take}")
        total -= what_i_will_take * coin

    return -1 if total else number_of_coins

print(makeChange([1, 2, 25], 37))

# print(makeChange([1256, 54, 48, 16, 102], 1453))
