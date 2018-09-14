# Uses python3

# Input Format. The  rst line contains an integer 𝑛. The second line contains integers 𝑣1 , 𝑣2 , . . . , 𝑣𝑛 
# separated by spaces.
# Constraints. 1≤𝑛≤20,1≤𝑣𝑖 ≤30forall𝑖.
# Output Format. Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, 
# and 0 otherwise.

# Sample 
# Input = 17 59 34 57 17 23 67 1 18 2 59
# Output = 1

import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

