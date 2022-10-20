# Python3 program to find the sum of
# N elements

# Function to perform desired operation
def operate(array, N) :
	Sum, index = 0, 0
	while(True) :
		Sum += array[index]
		index += 1
		if index < N :
		
			# backward jump of goto statement
			continue
		else :
			break
		
	# return the sum
	return Sum
	
# Get N
N, Sum = 5, 0

# Input values of an array
array = [ 1, 2, 3, 4, 5 ]

# Find the sum
Sum = operate(array, N)

# Print the sum
print(Sum)


