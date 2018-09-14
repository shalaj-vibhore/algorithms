# Uses python3

# Task. The goal in this code problem is to check whether an input sequence contains a majority element. 
# Input Format. The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative 
# integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
# Constraints. 1≤𝑛≤105;0≤𝑎𝑖 ≤109 for all 0≤𝑖<𝑛.
# Output Format. Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, 
# and 0 otherwise.

# Sample 
# Input = 2 3 9 2 2
# Output = 1

import sys

def get_majority_element(a, left, right):
    majority_dict={}
    max_item=None
    max_element_count=0
    for item in a:
        if item in majority_dict:
            majority_dict[item]+=1
            if majority_dict[item]>max_element_count:
                max_item = item
                max_element_count=majority_dict[item]
        else:
            majority_dict[item]=1
            if majority_dict[item]>max_element_count:
                max_item = item
                max_element_count=majority_dict[item]
    if max_element_count > float(((len(a))/2)):
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
