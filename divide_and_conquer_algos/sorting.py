# Uses python3

# Task. To force the given implementation of the quick sort algorithm to e ciently process sequences with 
# few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new 
# partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.
# Input Format. The  rst line of the input contains an integer 𝑛. The next line contains a sequence of 
# 𝑛 integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
# Constraints. 1≤𝑛≤105;1≤𝑎𝑖 ≤109 for all 0≤𝑖<𝑛.
# Output Format. Output this sequence sorted in non-decreasing order.


# Sample 
# Input = 2 3 9 2 2
# Output = 2 2 2 3 9

import sys
import random

def partition3(a, l, r):
    lt = l
    gt = r
    x = a[l]
    i = l
    while i <= gt:
        if a[i] < x:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > x:
            a[gt], a[i] = a[i], a[gt]
            gt -= 1
        else:
            i += 1
    return lt,gt


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1,m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
