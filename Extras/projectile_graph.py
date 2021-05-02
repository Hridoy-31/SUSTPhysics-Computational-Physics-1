import numpy as np

def Euler_Method(f, a, b, y0, step):
    t = np.linspace(a, b, step)
    h = t[1] - t[0]
    Y = [y0]
    N = len(t)
    n = 0
    y = y0
    while n <= N - 2:
        y = y + h * f(y, t[n])
        Y.append(y)
        n += 1
    Y = np.array(Y)
    return Y, t

def RK2(f, a, b, y0, step):
    t = np.linspace(a, b, step)
    h = t[1] - t[0]
    Y = [y0]
    N = len(t)
    n = 0
    y = y0
    while n <= N - 2:
        y_rk2 = y + h * 0.5 * f(y, t[n])
        y = y + h * f(y_rk2, t[n] + h * 0.5)
        Y.append(y)
        n += 1
    Y = np.array(Y)
    return Y, t
