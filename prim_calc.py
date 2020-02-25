#Uses Python3

import math

def prim_calc(n):
	num_opr = [0,0]+[math.inf]*(n-1)

	for i in range(2,n+1):
		t1,t2,t3 = [math.inf]*3
		t1 = num_opr[i-1]+1
		if i%2==0: 
			t2 = num_opr[i//2]+1
		if i%3==0: 
			t3 = num_opr[i//3]+1
		num_opr[i] = min(t1,t2,t3)

	print(num_opr[n])

	num = [n]
	while n!=1:
		if n%3 == 0 and num_opr[n]-1 == num_opr[n//3]:
			num += [n//3]
			n = n//3
		elif n%2 == 0 and num_opr[n]-1 == num_opr[n//2]:
			num += [n//2]
			n = n//2
		else:
			num += [n-1]
			n -= 1

	#num = reversed(num)
	num.reverse()
	print(" ".join(str(i) for i in num))


if __name__ == '__main__':
	n = int(input())
	prim_calc(n)
