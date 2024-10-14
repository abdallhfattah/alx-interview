#!/usr/bin/python3
"""
prime game
"""

# Declare the global variable to store the prime numbers
prime_numbers = []


def sieve(n):
    """
    This function calculates all prime numbers up to n using
    the Sieve of Eratosthenes and updates the global is_prime list.

    Args:
        n (int): The upper limit to find prime numbers.
    """
    prime = [True] * (n + 1)

    prime[0] = prime[1] = False

    # Apply Sieve of Eratosthenes to find primes
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for multiple in range(p * p, n + 1, p):
                prime[multiple] = False

    # filter out the prime numbers
    for i, is_prime in enumerate(prime):
        if is_prime:
            prime_numbers.append(i)


def lower_bound(arr, target):

    if len(arr) and arr[0] > target:
        return 1  # indicate ben wins

    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid
        else:
            right = mid - 1
    return left


# O(n * log(log(n)))
def isWinner(rounds, nums):
    """
    This function determines the winner based on rounds and numbers given.

    Args:
        rounds (int): Number of rounds of the game
        nums (list): List of numbers for each round
    """
    max_num = max(nums)
    sieve(max_num)

    def check_winner_for_this_round(number):
        index = lower_bound(prime_numbers, number)
        # print("number : " , number , "index : ",
        # index , ' Winner for this round : ' ,
        # "Ben" if index % 2 else "Maria")
        return -1 if index % 2 else 1

    winner = 0
    for num in nums:
        winner += check_winner_for_this_round(num)

    prime_numbers.clear()  # clear the global list

    if winner > 0:
        return "Maria"
    elif winner < 0:
        return "Ben"
    else:
        return None
