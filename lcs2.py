#Uses python3

import sys
import numpy as np
def lcs2(a, b):
    #write your code here
    n = len(a)
    m = len(b)
    L = np.zeros((n+1,m+1))

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            elif a[i-1] != b[j-1]:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[n][m]

if __name__ == '__main__':
    
    n = int(input())
    a = [int(i) for i in input().split()]

    m = int(input())
    b = [int(i) for i in input().split()]

    print(int(lcs2(a, b)))