# Uses python3
import numpy 

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    val = numpy.zeros((W+1, n+1))
    
    for we in range(1,W+1):
    	for i in range(1,n+1):
    		val[we][i] = val[we][i-1]
    		if  w[i-1] <= we:
    			temp_val = val[we - w[i-1]][i-1] + w[i-1]
    			if temp_val > val[we][i]:
    				val[we][i] = temp_val
    				#print(i)
    				#print(val)


    return val[W][n]



if __name__ == '__main__':
    W, n = [int(i) for i in input().split()]
    
    w = [int(i) for i in input().split()]
    #print(w)
    print(int(optimal_weight(W, w)))
    


