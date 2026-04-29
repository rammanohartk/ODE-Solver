import numpy as np


def EulerODE(f,t0,y0,nmax,h):
    '''
    # f:function
    # t0: starting time
    # y0: starting value
    # nmax: number of iteration
    # h : step size
    # Returns the values of t and y
    '''
    t = t0
    y = y0
    t_values = [t] # Collect data
    y_values = [y] # Collect data

    for i in range(1, nmax+1):
        y = y + f(t,y) * h 
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return  np.array(t_values), np.array(y_values)

