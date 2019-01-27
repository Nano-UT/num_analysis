import matplotlib.pyplot as plt
import numpy as np

def df(x):
    return(np.array([-x[1], x[0]]))

h = 0.5
xs = [np.array([1,0])]
i = 0
while(h * i <= 100):
    k1 = df(xs[i])
    k2 = df(xs[i] + k1 * h/ 2)
    k3 = df(xs[i] + k2 * h/ 2)
    k4 = df(xs[i] + k3 * h)
    xs.append(xs[i]+h*(k1+k2*2+k3*2+k4)/6)
    i += 1

p = [xs[i][0] for i in range(len(xs))]
q = [xs[i][1] for i in range(len(xs))]
plt.plot(p,q)
plt.xlabel('p')
plt.ylabel('q')
plt.title("Stride: "+str(h))
plt.show()
