# Uses python3

# Task. The goal of this problem is to implement the algorithm for computing the edit distance between two strings.
# Input Format. Each of the two lines of the input contains a string consisting of lower case latin letters. 
# Constraints. The length of both strings is at least 1 and at most 100.
# Output Format. Output the edit distance between the given two strings.

# Sample 
# Input = 
# editing
# distance
# Output = 5

def edit_distance(s, t):
    m = len(s)
    n= len(t)
    edit_mat = [[0 for x in range(n+1)] for x in range(m+1)]
 

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                edit_mat[i][j] = j    

            elif j == 0:
                edit_mat[i][j] = i    

            elif s[i-1] == t[j-1]:
                edit_mat[i][j] = edit_mat[i-1][j-1]
 

            else:
                edit_mat[i][j] = 1 + min(edit_mat[i][j-1],
                                         edit_mat[i-1][j],
                                         edit_mat[i-1][j-1])    
 
    return edit_mat[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
