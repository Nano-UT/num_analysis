import matplotlib.pyplot as plt

#微分方程式はdp/dt=-q, dq/dt=p)
#これを陰的Euler法の公式に当てはめると、p[t+h]=p[t]-h*q[t+h], q[t+h]=q[t]+h*p[t+h]
#すなわち、p[t+h]=p[t]-h*q[t+h]=p[t]-h*(q[t]+h*p[t+h])=p[t]-h*q[t]-h^2*p[t+h]
#したがって、(1+h^2)p[t+h]=p[t]-h*q[t] 同様にして(1+h^2)q[t+h]=q[t]+h*p[t]
#よって、漸化式はp[t+h]=(p[t]-h*q[t])/(1+h^2), q[t+h]=(q[t]+h*p[t])/(1+h^2)である。

h = 0.7
p, q = [1], [0]
i = 0
while(h * i <= 100):
    p.append((p[i] - h * q[i])/(1+h**2))
    q.append((q[i] + h * p[i])/(1+h**2))
    i += 1

plt.rcParams["font.family"] = "IPAexGothic"
plt.plot(p,q)
plt.xlabel('p')
plt.ylabel('q')
plt.title("陰的Euler法 刻み幅: "+str(h))
plt.show()
