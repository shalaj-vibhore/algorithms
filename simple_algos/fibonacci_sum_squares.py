# Uses python3

# Task. Compute the last digit of 𝐹02 +𝐹12 +···+𝐹𝑛2. 
# Input Format. Integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 1018.
# Output Format. The last digit of 𝐹02 + 𝐹12 + · · · + 𝐹𝑛2.

# Sample 
# Input = 1234567890 
# Output = 0

from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
