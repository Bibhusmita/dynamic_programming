# Uses python3
from itertools import product
import sys
w = [...]



def partition3(A):
    for partition in product(range(0,3), repeat=len(A)):
        sums = [0] * 3
        sums = [sum(A[k] for k in range(len(A)) if partition[k] == i) for i in range(0,3)]
        #print(sums)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0





if __name__ == '__main__':
    n = input()
    A = [int(i) for i in input().split()]
    print(partition3(A))
    #print(partition(A))



