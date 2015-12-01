__author__ = 'Prabuddha'
from numpy import genfromtxt
import numpy as np
from matplotlib import pyplot as plt
# pollution data
Data = genfromtxt(open('whitewines.csv', 'r'), dtype=float, delimiter=',')[1:]
Labels = Data[:, 11]
# Data = Data[:, [0, 11]]
header = genfromtxt(open('whitewines.csv', 'r'), delimiter=',', dtype=None)[0]
header = header[1:]
header = header[np.newaxis, :]

N = Data.shape[0]
data = Data[:500, [0, 11]]
print data
labels = ['point{0}'.format(i) for i in range(N)]
plt.subplots_adjust(bottom=0.1)
plt.scatter(
    data[:, 0], data[:, 1], marker='o',
    cmap=plt.get_cmap('Spectral'))
for label, x, y in zip(labels, data[:, 0], data[:, 1]):
    plt.annotate(label,xy=(x, y), xytext=(-20, 20),textcoords='offset points', ha='right', va='bottom', bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
# print label
plt.show()
