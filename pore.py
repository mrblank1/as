import numpy as np 
import matplotlib.pyplot as plt
t=np.linspace(0,10,100)
y=[(1+i)/(i**(i/(i-1))) for i in t]
plt.plot(t,y)
plt.show()