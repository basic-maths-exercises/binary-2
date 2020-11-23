import numpy as np

def get_binary( N, index ) : 
  binary = np.zeros(N)
  # Your code goes here
  
  return binary
  
  
# You shouldn't need to modify this code.  Once you have your function 
# working running this code will allow you to test if it is working
ndigits = 3
for i in range(2**ndigits) :
  print( get_binary(ndigits,i) )
