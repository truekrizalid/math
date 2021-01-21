import numpy as np

import scipy.integrate 
import matplotlib.pyplot as plt

def sys(X,t=0):
    X[0]= X[0]+X[1]+10*np.cos(t)
    X[1]=3*X[0]-X[1]-10*np.sin(t)

    return X

t = np.linspace(0,100,1001)

t =odient(X, 1,1,t)
print(t)