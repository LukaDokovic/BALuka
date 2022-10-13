
# Fresnel Funktion weiter aufgeteilt in seine Originale

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel
import tensorflow as tf


t = np.linspace(0.3,5,100)
x,y =(fresnel(t))
y2 = np.square(tf.math.special.fresnel_cos(t))  #-0.3
#Bsp: np.sqrt(tf.math.special.fresnel_cos(t)) verändert alles
x1 = np.square(tf.math.special.fresnel_sin(t))


plt.plot(x, y, 'red',x1 ,y2, 'green')
plt.show()


"""
# Fresnel Funktionen aufgeteilt

import numpy as np
from scipy.special import fresnel
import matplotlib.pyplot as plt

t = np.linspace(0, 5.0, 201)
ss, cc = fresnel(t / np.sqrt(np.pi / 2))
scaled_ss = np.sqrt(np.pi / 2) * ss
scaled_cc = np.sqrt(np.pi / 2) * cc
plt.plot(t, scaled_cc, 'g--', t, scaled_ss, 'r-', linewidth=2)
plt.grid(True)
plt.show()
"""



"""
#Normalenvektor veranschaulichen
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel
import tensorflow as tf


t = np.linspace(0.3,5,100)
x,y =(fresnel(t))
dy = -np.gradient(y)
dx = np.gradient(x)


plt.quiver(x,y,dy,dx)
plt.plot(x, y, 'red')
plt.show()
"""

"""
#Normalenvektor nicht normiert 
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel
import tensorflow as tf


t = np.linspace(0,1,10)
x,y =(fresnel(t))
vy = -np.gradient(y)
vx = np.gradient(x)
dx = x + vx
dy = y - vy
plt.quiver(x,y,vy,vx)

plt.plot(x, y, 'red',dx,dy, 'green')

plt.show()
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel
import tensorflow as tf


t = np.linspace(0,5,100)
x,y =(fresnel(t))
gradienty = -np.gradient(y)
gradientx = np.gradient(x)
dx = x + gradientx
dy = y - gradienty
plt.quiver(x,y,gradienty,gradientx)

#np.linalg.norm


plt.plot(x, y, 'red',dx,dy, 'green')

plt.show()
"""
