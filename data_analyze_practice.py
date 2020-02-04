import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data = np.arange(10)
plt.plot(data)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
plt.plot(np.random.randn(50).cumsum(),'k--')
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

ax4 = fig.add_subplot(2,2,4)

ax2.hist(np.random.randn(100) ,color = 'g' ,alpha = 0.3)

ax3.scatter(np.random.randn(100),np.random.randn(100))




