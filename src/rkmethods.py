import numpy as np

# Classic 4th order method
def rk4(f,t0,y0,nmax,h):
    '''
    # f:function
    # t0: starting time
    # y0: starting value of y
    # nmax: number of iteration
    # h : step size
    # Returns the values of t and y
    '''
    t = t0
    y = y0
    t_values = [t] # Collect data
    y_values = [y] # Collect data

    for i in range(1, nmax+1):
        k1 = f(t,y)*h
        k2 = f(t + h/2, y + k1/2)*h
        k3 = f(t + h/2, y +k2/2)*h
        k4 = f(t + h, y + k3)*h
        k =1/6*k1 + 1/3*k2 + 1/3*k3 + 1/6*k4
        y = y + k
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return  np.array(t_values), np.array(y_values)

# RK5 method
def rk5(f,t0,y0,nmax,h):
    '''
    # f:function
    # t0: starting time
    # y0: starting value of y
    # nmax: number of iteration
    # h : step size
    # Returns the values of t and y
    '''
    t = t0
    y = y0
    t_values = [t] # Collect data
    y_values = [y] # Collect data

    for i in range(1, nmax+1):
        k1 = f(t,y)*h
        k2 = f(t + h/4, y + k1/4)*h
        k3 = f(t + h*3/8, y + k1*3/32 +k2*9/32)*h
        k4 = f(t + h*12/13, y + k1*1932/2197 - k2*7200/2197+ k3*7296/2197)*h
        k5 = f(t + h, y +  k1*439/216 - k2*8+ k3*3680/513- k4*845/4104)*h
        k6 = f(t + h/2, y - k1*8/27 + k2*2 - k3*3544/2565 + k4*1859/4104 - k5*11/40)*h
        k =16/135*k1 + 0*k2 + 6656/12825*k3 + 28561/56430*k4 - 9/50*k5 + 2/55*k6
        y = y + k
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return  np.array(t_values), np.array(y_values)