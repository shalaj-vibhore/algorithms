# Uses python3

# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format. The  rst line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. 
# The next 𝑛 lines de ne the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the 
# value and the weight of 𝑖-th item, respectively.
# Constraints. 1≤𝑛≤103,0≤𝑊 ≤2·106;0≤𝑣𝑖 ≤2·106,0<𝑤𝑖 ≤2·106 forall1≤𝑖≤𝑛.Allthe numbers are integers.
# Output Format. Output the maximal value of fractions of items that  t into the knapsack. The absolute 
# value of the di erence between the answer of your program and the optimal value should be at most 10−3. 
# To ensure this, output your answer with at least four digits after the decimal point 


# Sample 
# Input = 
# 1 10
# 500 30 
# Output = 166.6667

import sys

def get_optimal_value(capacity, weights, values):
    w_v=[float(values[i]/weights[i]) for i in range(len(weights))]
    total_value=0
    while capacity!=0:
        if(len(w_v)==0):
            break;
        max_w_v = max(w_v)
        index = w_v.index(max_w_v)
        considered_weight =weights[index] 
        considered_value = values[index]
        if capacity < considered_weight:
            total_value+=capacity*max_w_v
            capacity=0
        else:
            total_value+=considered_value
            capacity-=considered_weight
        del(w_v[index])
        del(weights[index])
        del(values[index])
    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
