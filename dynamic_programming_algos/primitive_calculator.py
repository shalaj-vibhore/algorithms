# Uses python3

# Task. Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛 starting 
# from the number 1.
# Input Format. The input consists of a single integer 1 ≤ 𝑛 ≤ 106.
# Output Format. In the  rst line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1. 
# In the second line output a sequence of intermediate numbers. That is, the second line should contain 
# positive integers 𝑎0,𝑎2,...,𝑎𝑘−1 such that 𝑎0 =1,𝑎𝑘−1 =𝑛 and for all 0≤𝑖<𝑘−1,𝑎𝑖+1 is equal to either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖. 
# If there are many such sequences, output any one of them.

# Sample 
# Input = 5 
# Output = 
# 3
# 1 2 4 5

import sys

def optimal_sequence(n):
    v = [0]*(n+1)  

    for i in range(1,n):
        if v[i+1] == 0 : 
            v[i+1] = v[i] + 1 
        if (i+1)%2==0:
            if v[i+1]>v[int((i+1)/2)]+1:
                v[i+1]=v[int((i+1)/2)]+1
        if (i+1)%3==0:
            if v[i+1]>v[int((i+1)/3)]+1:
                v[i+1]=v[int((i+1)/3)]+1


    solution = []
    while n > 1:
        solution.append(n)
        if v[n-1] == v[n] - 1: 
            n = n-1
        elif n%2 == 0 and v[n//2] == v[n] -1: 
            n = n//2
        elif n%3 == 0 and v[n//3] == v[n] -1: 
            n = n//3
    solution.append(1)
    return reversed(solution)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
