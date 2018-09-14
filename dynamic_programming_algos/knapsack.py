# Uses python3

# Task. Given 𝑛 gold bars,  nd the maximum weight of gold that  ts into a bag of capacity 𝑊 .
# Input Format. The  rst line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars
# of gold. The next line contains 𝑛 integers 𝑤0 , 𝑤1 , . . . , 𝑤𝑛−1 de ning the weights of the bars of gold. Constraints. 1 ≤ 𝑊 ≤ 104; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0,...,𝑤𝑛−1 ≤ 105.
# Output Format. Output the maximum weight of gold that  ts into a knapsack of capacity 𝑊 .

# Sample 
# Input = 
# 10 3 
# 1 4 8
# Output = 9

import sys

def optimal_weight(W, w):
    n= len(w)
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    for i in range(n+1):
        for wt in range(W+1):
            if i==0 or wt==0:
                K[i][wt] = 0
            elif w[i-1] <= wt:
                K[i][wt] = max(w[i-1] + K[i-1][wt-w[i-1]],  K[i-1][wt])
            else:
                K[i][wt] = K[i-1][wt]
 
    return K[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
