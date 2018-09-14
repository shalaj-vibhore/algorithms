# Uses python3

# Task. The goal in this problem is to  nd the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
# Input Format. The input consists of a single integer 𝑚.
# Constraints. 1 ≤ 𝑚 ≤ 103.
# Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.

# Coin Denomination : 1, 5, 10
# Sample 
# Input = 28
# Output = 6

import sys

def get_change(m):
    coins=0
    while m!=0:
        if m>=10:
            coins+=int(m/10)
            m=m%10
        elif m>=5:
            coins+=int(m/5)
            m=m%5
        else:
            coins+=int(m/1)
            m=0
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
