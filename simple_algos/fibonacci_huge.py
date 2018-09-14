# Uses python3

# Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚). 
# Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space). Constraints. 1≤𝑛≤1018,2≤𝑚≤103.
# Output Format. Output 𝐹𝑛 mod 𝑚.

# Sample 
# Input = 2816213588 239
# Output = 151

import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
