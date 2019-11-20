from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math


ax = plt.axes(projection="3d")

def z_function(x, y):
    return (x ** 2 + y ** 2)** (1/2)

x = np.linspace(0, 6, 50)
y = np.linspace(0, 6, 50)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)


ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='green', rstride = 1, cstride = 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
