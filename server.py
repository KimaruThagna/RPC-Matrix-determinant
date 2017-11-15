import rpyc
from rpyc.utils.server import ThreadedServer #import a threaded server from the rpyc library function to setup a threaded serrver


def det(l):
    n=len(l) #order of the matrix
    if (n>2): # if matrix is not a 2X2 matrix....use cofactor expansion method to calculate det
        i=1
        t=0
        sum=0 #initialize determinant
        while t<=n-1:
            d={} # empty dictionary
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[] # create empty list as value for dictionary entry at position t1
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m]) # concatenation of the value at position [t] [m]
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1)) # calculation of dterminant using cofactor expansion
            # recursion used in the case of a matrix of an order larger than 3
            i=i*(-1)
            t+=1
        return sum #retuen determinant
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0]) # calculation of a 2X2 matrix

class MyService(rpyc.Service): # create a class to hold the exposed function which will be called by the client during the RPC communication
	def exposed_compute(self,matrix): # exposed is a prefix to make the function visible to the client
		determinant=det(matrix) # call determinant function
		return determinant # return result

t = ThreadedServer(MyService, port = 7001)# handles each request using a new thread as opposed to handling requests with a new process
t.start() # start server