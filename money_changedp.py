# Uses python3
import math

def get_change(m):
	minCoins = [0] + [math.inf]*m
	for j in range(1,m+1):
		for i in [1,3,4]:
			if j>=i:
				c = minCoins[j-i]+1
				if c < minCoins[j]:
					minCoins[j] = c

	return minCoins[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))