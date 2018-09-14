# Uses python3

# Task. Given an integer 𝑛,  nd the last digit of the sum 𝐹0 +𝐹1 +···+𝐹𝑛. 
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 1018.
# Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.

# Sample 
# Input = 100 
# Output = 5

import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))