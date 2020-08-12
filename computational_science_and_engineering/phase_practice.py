import matplotlib.pyplot as plt
import numpy as np
# show plots in notebook

# define system in terms of separated differential equations
def f(x,y):
    return y
def g(x,y):
    return 2*np.sin(x)

def sys(iv1, iv2, dt, time):
    x = np.zeros(time)
    y = np.zeros(time)
    dt = 0.01
    x[0]= iv1
    y[0]= iv2
    for i in range(time-1):
        x[i+1]=x[i] + (f(x[i],y[i])) * dt
        y[i+1]=y[i] +  (g(x[i],y[i])) * dt

    return x,y

x,y =sys(3.14*2, 0.1, 0.01, 1000)
x1,y1 =sys(3.14*3,0.1,0.01,1000)
#plot
fig = plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace = 0.5, hspace = 0.3)
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x, 'r-', label='y1')
ax1.plot(y, 'b-', label='y2')
#ax1.plot(z, 'g-', label='prey')
ax1.set_title("Dynamics in time")
ax1.set_xlabel("time")
ax1.grid()
ax1.legend(loc='best')

ax2.plot(x, y, color="blue")
ax2.plot(x1,y1,color="red")
ax2.set_xlabel("x")
ax2.set_ylabel("y")  
ax2.set_title("Phase space")
ax2.grid()
plt.show()