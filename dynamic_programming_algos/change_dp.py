# Uses python3

# Input Format. Integer money.
# Output Format. The minimum number of coins with denominations 1, 3, 4 that changes money. 
# Constraints. 1 ≤ money ≤ 103.

# Denomination = 1, 3, 4
# Sample 
# Input = 34
# Output = 9

import sys

def get_change(m):
    coins=[1,3,4]
    min_coin_list = [999999999999999999]*(m+1)
    min_coin_list[0]=0
    for coin in coins:
        for i in range(1,m+1):
            if i >= coin:
                coin_count = min_coin_list[i-coin]+1
                if coin_count<min_coin_list[i]:
                    min_coin_list[i]=coin_count
    return min_coin_list[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
