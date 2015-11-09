# run code in ipython as:     run -d debugDemo.py
# n: to execute next line, s to step into funciton
# r: to  retun to end of function.
# until: to execute until next line
# bt: to see function call flow or stack frame
# up: to go to up in  frame by one
# down: to go  down in the frame
# b: to put break points like
#      b 20 to put break point at line number 20 in current file
#      b Util/linearAlgerba.py:33 to put break at line number 33 in
#                            linearAlgebra.py file in side Fiolder Util

import numpy as np
import matplotlib.pyplot as plt
import Util.linearAlgebra as LA # how to orgnaise code in folder
                                # keep a __init__.py file in folder 
def testPCA():  
  A = np.array([ [2.4,0.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,0.9],
            [2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1] ])
  coeff, score, latent = LA.princomp(A.T) # how to go inside press s
  plt.figure()
  plt.subplot(121)
  # every eigenvector describe the direction
  # of a principal component.
  m = np.mean(A,axis=1)
  plt.plot([0, -coeff[0,0]*2]+m[0], [0, -coeff[0,1]*2]+m[1],'--k')
  plt.plot([0, coeff[1,0]*2]+m[0], [0, coeff[1,1]*2]+m[1],'--k')
  plt.plot(A[0,:],A[1,:],'ob') # the data
  plt.axis('equal')
  plt.subplot(122)
  # new data
  plt.plot(score[0,:],score[1,:],'*g')
  plt.axis('equal')
  plt.show()

  ## use case for until
  muParam = [i*i for i in xrange(1, 10)]
  wgt = 1
  muParamNormalized = LA.normalize(muParam, weight= wgt)
  print muParamNormalized

  
  

if __name__ == '__main__':
  testPCA()
