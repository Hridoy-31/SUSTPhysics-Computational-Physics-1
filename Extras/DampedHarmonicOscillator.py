from numpy import *
from pylab import *
from scipy.linalg import *

time = linspace(0.0, 10.0, 10000)
height = exp(-time / 3.0) * sin(time * 3)
figure()
plot(time, height, 'm-')
plot(time, 0.3 * sin(time * 3), 'g-')
legend(['damped', 'constant amplitude'], loc='upper right')
xlabel('Time (s)')
show()
