# python3

# Maximum Pairwise Product Problem
# Find the maximum product of two distinct num-bers in a sequence of non-negative integers.

# Input: A sequence of non-negative integers.
# Output: The maximum value that can be obtained by multiplying two different elements from the se-quence.

# Sample 
# Input = 1 2 3 
# Output = 6

def max_pairwise_product(numbers,n):
    numbers.sort()
    max_product = numbers[n-1]*numbers[n-2]

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers,input_n))
