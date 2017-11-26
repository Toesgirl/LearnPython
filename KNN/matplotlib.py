import file2matrix
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


a, b = file2matrix.file2matrix("datingTestSet2.txt")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(a[:, 0], a[:, 1], 15.0*np.array(b), 15.0*np.array(b))
plt.show()


