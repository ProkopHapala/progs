
import sys
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt( sys.argv[1], skip_header=1 )
data = np.transpose(data)

plt.plot(data[0], data[1])

plt.show()