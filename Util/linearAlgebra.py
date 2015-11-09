from __future__ import division
import numpy as np

import numpy as np
# http://glowingpython.blogspot.com/2011/07/principal-component-analysis-with-numpy.html



def princomp(A):
  ''' This function performs principle component analysis
  on matrix A_nxp. Rows of A correspond to observations,
  columns to variables.
  Returns :  
  coeff :
    is a p-by-p matrix, each column containing coefficients 
    for one principal component.
  score : 
    the principal component scores; that is, the representation 
    of A in the principal component space. Rows of SCORE 
    correspond to observations, columns to components.
  latent : 
    a vector containing the eigenvalues 
    of the covariance matrix of A.
  '''
  # computing eigenvalues and eigenvectors of covariance matrix
  M = (A-np.mean(A.T,axis=1)).T # subtract the mean (along columns)
  [latent, coeff] = np.linalg.eig(np.cov(M)) # attention:not always sorted
  score = np.dot(coeff.T,M) # projection of the data in the new space
  return coeff, score, latent

def normalize(paramsList, weight = 1):
  sumParms = sum(paramsList)
  weight = sumParms*weight
  normalizeParam = [i/(weight) for i in paramsList]

  return normalizeParam



  
