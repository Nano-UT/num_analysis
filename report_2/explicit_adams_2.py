import matplotlib.pyplot as plt

#漸化式はp[t+2*h]=p[t+h]-h*(3*q[t+h]-q[t])/2, q[t+2*h]=q[t+h]+h*(3*p[t+h]-p[t])/2である。

h = 0.1
p, q = [1], [0]
p.append(p[0] - h * q[0])
q.append(q[0] + h * p[0])
i = 1

while(h * i <= 100):
    p.append(p[i]-h*(3*q[i]-q[i-1])/2)
    q.append(q[i]+h*(3*p[i]-p[i-1])/2)
    i += 1

plt.plot(p,q)
plt.xlabel('p')
plt.ylabel('q')
plt.title("Stride: "+str(h))
plt.show()
