import matplotlib.pyplot as plt

h = 0.7
p, q = [1], [0]
i = 0
while(h * i <= 100):
    p.append(p[i] - h * q[i])
    q.append(q[i] + h * p[i])
    i += 1

plt.rcParams["font.family"] = "IPAexGothic"
plt.plot(p,q)
plt.xlabel('p')
plt.ylabel('q')
plt.title("陽的Euler法 刻み幅: "+str(h))
plt.show()
