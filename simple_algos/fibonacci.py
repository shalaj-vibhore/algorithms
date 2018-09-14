# Uses python3

# Task. Given an integer 𝑛,  nd the 𝑛th Fibonacci number 𝐹𝑛. Input Format. 
# The input consists of a single integer 𝑛. 
# Constraints. 0 ≤ 𝑛 ≤ 45.
# Output Format. Output 𝐹𝑛.

# Sample 
# Input = 10
# Output = 55


def calc_fib(n):
    n_1=0
    n_2=1
    fib_sum=0
    for i in range(0,n):
        if (n <= 1):
            return n
        fib_sum=n_1+n_2
        n_2=n_1
        n_1=fib_sum
    
    return fib_sum

n = int(input())
print(calc_fib(n))
