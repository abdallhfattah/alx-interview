class PrimeGame:
    def __init__(self):
        self.prime_numbers = []

    def sieve(self, n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                for multiple in range(p * p, n + 1, p):
                    prime[multiple] = False

        self.prime_numbers = [i for i, is_prime in enumerate(prime) if is_prime]

    def lower_bound(self, target):

        if self.prime_numbers[-1] < target:
            return len(self.prime_numbers) - 1

        if self.prime_numbers[0] > target:
            return 1 # indicate that ben won

        left, right = 0, len(self.prime_numbers)
        while left < right:
            mid = (left + right) // 2
            if self.prime_numbers[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def check_winner_for_this_round(self, number):
        index = self.lower_bound(number)
        # print("index : " , index)
        return -1 if index % 2 else 1

    def is_winner_helper(self, x, nums):

        if x <= 0 or nums is None or x != len(nums):
            # print("i actaully stoped here")
            return None

        max_num = max(nums)
        self.sieve(max_num)

        # print("prime numbers: " ,self.prime_numbers)

        winner = 0
        for num in nums:
            winner += self.check_winner_for_this_round(num)

        self.prime_numbers.clear()
        # print("score: " , winner)
        if winner > 0:
            return "Maria"
        elif winner < 0:
            return "Ben"
        else:
            return None


def is_winner(rounds, nums):
    prime = PrimeGame()
    return prime.is_winner_helper(rounds, nums)


if __name__ == '__main__':
    # print(is_winner(2, [1, 2]))
    print(is_winner(3, [4, 4, 4]))