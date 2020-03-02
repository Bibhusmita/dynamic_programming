#Uses python3


import numpy as np
def lcs3(a, b, c):
    #write your code here
    n = len(a)
    m = len(b)
    o = len(c)
    L = np.zeros((n+1,m+1,o+1))

    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(1,o+1):
                if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                elif a[i-1] != b[j-1] or b[j-1] != c[k-1] or a[i-1] != c[k-1]:
                    L[i][j][k] = max(L[i-1][j][k], L[i][j-1][k], L[i][j][k-1])

    return L[n][m][o]

if __name__ == '__main__':
    
    n = int(input())
    a = [int(i) for i in input().split()]

    m = int(input())
    b = [int(i) for i in input().split()]


    o = int(input())
    c = [int(i) for i in input().split()]

    print(int(lcs3(a, b, c)))