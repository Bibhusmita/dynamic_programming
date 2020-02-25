# Uses python3
import numpy

def edit_distance(s, t):
    m = len(s)
    n = len(t)

    dp_matrix = numpy.zeros((m+1,n+1))

    for i in range(0,m+1):
    	for j in range(0,n+1):
    		if i == 0:
    			dp_matrix[i][j] = j

    		elif j == 0:
    			dp_matrix[i][j] = i

    		else:
    			ins = dp_matrix[i][j-1]+1
	    		dlt = dp_matrix[i-1][j]+1
	    		mat = dp_matrix[i-1][j-1]
	    		if s[i-1] == t[j-1]:
	    			dp_matrix[i][j]=min(ins,dlt,mat)
	    		else:
	    			dp_matrix[i][j] = min(ins,dlt,mat+1)
    		 
    return int(dp_matrix[m][n])

if __name__ == "__main__":
    print(edit_distance(input(), input()))