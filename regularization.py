 import numpy as np
 import matplotlib.pyplot as plt
 
 
 x = np.array([ 2.0, 4.0,  5.0, 5.3, 6])
 y = np.array([ 0.9, -0.8, -1.0,-0.7, -0.5])
 z = np.polyfit(x, y, 2)


xp = np.linspace(-2, 6, 100)
p = np.poly1d(z)
p4 = np.poly1d(np.polyfit(x, y, 4))
plt.plot(x, y, '.', xp, p(xp), '-', xp, p4(xp), '--')
plt.ylim(-3,3)

