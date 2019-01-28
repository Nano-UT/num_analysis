import matplotlib.pyplot as plt

#微分方程式はdp/dt=-q, dq/dt=p)
#これを台形則の公式に当てはめると、p[t+h]-p[t]=(-h*q[t+h]-h*q[t])/2, q[t+h]-q[t]=(h*p[t+h]+h*p[t])/2
#すなわち、p[t+h]=p[t]+(-h*q[t+h]-h*q[t])/2=p[t]+(-h*(q[t]+(h*p[t+h]+h*p[t])/2)-h*q[t])/2=p[t]-h*q[t]-h^2*p[t+h]/4-h^2*p[t]/4
#したがって、(1+h^2/4)p[t+h]=p[t]-h^2*p[t]/4-h*q[t] 同様にして(1+h^2/4)q[t+h]=q[t]-h^2*q[t]/4+h*p[t]
#よって、漸化式はp[t+h]=((1-h^2/4)p[t]-h*q[t])/(1+h^2/4), q[t+h]=((1-h^2/4)q[t]+h*p[t])/(1+h^2/4)である。

h = 0.7
p, q = [1], [0]
i = 0
while(h * i <= 100):
    p.append(((1-h**2/4)*p[i] - h * q[i])/(1+h**2/4))
    q.append(((1-h**2/4)*q[i] + h * p[i])/(1+h**2/4))
    i += 1

plt.rcParams["font.family"] = "IPAexGothic"
plt.plot(p,q)
plt.xlabel('p')
plt.ylabel('q')
plt.title("台形則 刻み幅: "+str(h))
plt.show()
