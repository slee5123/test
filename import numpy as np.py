import numpy as np
import scipy as sp
import control.matlab as c
from control.matlab import *
from control.matlab import rlocus,sisotool,tf
from numpy import roots
import matplotlib.pyplot as plt
s=c.tf([1,0],[1])
h=(-0.1*s-0.0198)/(s**3+0.46*(s**2)+0.0401*s)*-0.2
H=h.feedback(1)
t=np.arange(0,100.01,0.01)
(y,t)=c.step(H,t)
plt.plot(t,y)
plt.show()


tsettle=t[y>1.05 | y<0.95][-1]
print(tsettle)