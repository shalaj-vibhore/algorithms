# Uses python3

# Task. Given two integers 𝑎 and 𝑏,  nd their least common multiple.
# Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space. Constraints. 1≤𝑎,𝑏≤2·109.
# Output Format. Output the least common multiple of 𝑎 and 𝑏.

# Sample 
# Input = 28851538 1183019
# Output = 1933053046

import sys

def gcd_naive(a, b):
    if b==0:
        return a
    if a>=b:
        return gcd_naive(b,a%b)
    else:
        return gcd_naive(a,b%a)

def lcm_naive(a, b):
    return int((a*b)//gcd_naive(a,b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

