# Uses python3
import math
import numpy as np

d = []
op = []
n = 0

def evalt(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_max(i,j,m,M):
    #write your code here
    min_ = math.inf
    max_ = -math.inf
    for k in range(i,j):
        a = evalt(M[i][k],op[k],M[k+1][j])
        b = evalt(m[i][k],op[k],m[k+1][j])
        c = evalt(M[i][k],op[k],m[k+1][j])
        d = evalt(m[i][k],op[k],M[k+1][j])
        min_ = min(min_,a,b,c,d)
        max_ = max(max_,a,b,c,d)

    return min_ , max_

def get_maximum_value(A):
    A = list(A)
    
    for i in range(len(A)):
        if i % 2 == 0:
            d.append(int(A[i]))
        else:
            op.append(A[i])

    n = int(len(d))
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]
    for i in range(0,n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1,n):
        for i in range(0,n-s):
            j = i+s
            m[i][j],M[i][j] = min_max(i,j,m,M)
    return M[0][n-1]   
    


if __name__ == "__main__":
    print(get_maximum_value(input()))
