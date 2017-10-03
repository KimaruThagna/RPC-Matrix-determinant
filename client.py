import rpyc

proxy = rpyc.connect('localhost', 7001) # connection function to connect to server by creation of an object
order =int(input('Enter the matrix order')) #get order of matrix from user and convert to integer
matrix=[ [0 for i in range(order)] for j in range(order) ] # initialization of matrix
# creates a matrix of the specified order but padded with 0s
print (matrix)
for x in range(order):
	for y in range(order):
		matrix[x][y]=int(input('Enter matrix value')) # this prompts the user for values and fills te matrix with those values instead.
		# x is the row index y is the column index
print ('Your',order,'by',order,'matrix')
print (matrix)
print('\nYour determinant\n')
determinant = proxy.root.compute(matrix) # calls the proxy object which calls the root.compute function
#root accesses the rpyc service class created in the server script and compute is the function in the server class
# compute function had a prefix keyword exposed so that it can be availed to the client from the server side
print (determinant)
