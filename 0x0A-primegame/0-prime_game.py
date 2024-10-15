#!/usr/bin/python3
"""
Module to find a winner of the prime game.
"""

from typing import List, Optional


class PrimeGame:
    """
    PrimeGame class that controls the game logic for finding the winner.
    """

    def __init__(self):
        """
        Initializes the PrimeGame class by creating an empty list of prime numbers.
        """
        self.prime_numbers: List[int] = []

    def sieve(self, n: int) -> None:
        """
        Implements the Sieve of Eratosthenes to find all prime numbers less than or equal to 'n'.
        
        Args:
            n (int): The upper limit for finding prime numbers.
        """
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                for multiple in range(p * p, n + 1, p):
                    prime[multiple] = False

        self.prime_numbers = [i for i, is_prime in enumerate(prime) if is_prime]

    def lower_bound(self, target: int) -> int:
        """
        A custom binary search (lower bound) to find the index of the largest prime number less than or equal to 'target'.
        
        Args:
            target (int): The number for which to find the largest prime less than or equal to it.
        
        Returns:
            int: The index of the largest prime number less than or equal to 'target'.
                 If 'target' is smaller than the smallest prime, it returns 1, indicating Ben wins.
        """
        if self.prime_numbers[-1] < target:
            return len(self.prime_numbers) - 1

        if self.prime_numbers[0] > target:
            return 1  # indicate that Ben won

        left, right = 0, len(self.prime_numbers)
        while left < right:
            mid = (left + right) // 2
            if self.prime_numbers[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def check_winner_for_this_round(self, number: int) -> int:
        """
        Determines the winner for a single round based on the given number.
        
        Args:
            number (int): The current number to check the winner for this round.
        
        Returns:
            int: -1 if Ben wins this round, 1 if Maria wins this round.
        """
        index = self.lower_bound(number)
        return -1 if index % 2 else 1

    def is_winner_helper(self, x: int, nums: List[int]) -> Optional[str]:
        """
        Helper function to determine the overall winner after 'x' rounds based on the provided numbers in 'nums'.
        
        Args:
            x (int): The number of rounds.
            nums (List[int]): The list of numbers for each round.
        
        Returns:
            Optional[str]: The name of the winner ("Maria" or "Ben") or None if no winner.
        """
        if x <= 0 or nums is None or x != len(nums):
            return None

        max_num = max(nums)
        self.sieve(max_num)

        winner = 0
        for num in nums:
            winner += self.check_winner_for_this_round(num)

        self.prime_numbers.clear()

        if winner > 0:
            return "Maria"
        elif winner < 0:
            return "Ben"
        else:
            return None


def is_winner(rounds: int, nums: List[int]) -> Optional[str]:
    """
    Function to determine the winner of the game after a number of rounds.
    
    Args:
        rounds (int): The number of rounds to be played.
        nums (List[int]): A list of numbers for each round.
    
    Returns:
        Optional[str]: The name of the winner ("Maria" or "Ben") or None if no winner.
    """
    prime = PrimeGame()
    return prime.is_winner_helper(rounds, nums)
