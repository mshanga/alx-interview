#!/usr/bin/python3
""" Prime Game  """

def isWinner(x, nums):
    """ Returns the winner of the Prime Game """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
        
        # Initialize a set to represent the remaining numbers
        remaining = set(range(2, n + 1))

        maria_turn = True
        while True:
            prime_found = False
            for num in remaining:
                if is_prime(num):
                    prime_found = True
                    prime = num
                    break
            if not prime_found:
                break

            # Remove prime and its multiples
            remaining.difference_update(range(prime, n + 1, prime))

            if maria_turn:
                maria_turn = False
            else:
                maria_turn = True

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return "None"

# Example usage
x = 3
nums = [4, 5, 1]
winner = isWinner(x, nums)
print(winner)  # Output: "Ben"
