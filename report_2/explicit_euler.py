import matplotlib.pyplot as plt

h = 0.05
p, q = [1], [0]
i = 0
while(h * i <= 100):
    p.append(p[i] - h * q[i])
    q.append(q[i] + h * p[i])
    i += 1

plt.plot(p,q)
plt.xlabel('p')
plt.ylabel('q')
plt.title("Stride: "+str(h))
plt.show()
