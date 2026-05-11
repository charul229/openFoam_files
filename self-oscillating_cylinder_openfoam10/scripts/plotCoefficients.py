'''
Script for plotting force coefficients from forces on solids obtianed from OpenFOAM simulations.

Developed for OpenCFD's version OpenFOAM-2312

Author: Dr Chennakesava Kadapa

Date: 04/Apr/2026
'''

import matplotlib.pyplot as plt
import numpy as np
from pylab import *

params = {'axes.labelsize': 14,
     'legend.fontsize': 14,
     'xtick.labelsize': 14,
     'ytick.labelsize': 14}
     
rcParams.update(params)     


filename='../postProcessing/forces/0/force.dat'

with open(filename) as f:
    data = f.readlines()[4:]

N = shape(data)[0]

timearray = np.zeros(N)
Fx = np.zeros(N)
Fy = np.zeros(N)
Fz = np.zeros(N)

ind=0
for item in data:
    result1 = item.split('\n')[0]
    #print(result1)
    result2 = result1.split()
    #print(result2)
    timearray[ind] = float(result2[0])
    #
    Fx[ind] = float(result2[1])
    Fy[ind] = float(result2[2])
    Fz[ind] = float(result2[3])
    ind = ind+1

rho = 1.0 # density
D   = 1.0 # diameter
A   = D   # projected area
U   = 1.0 # reference velocity
#mu  = 0.01 # dynamic viscosity

factor = 0.5*rho*A*U**2

CD = Fx/factor
CL = Fy/factor

plt.figure(2)
plt.plot(timearray, CD, '-', color='k', linewidth=2.0, markersize=4.0)
plt.ylabel('CD',fontsize=14)
plt.axis([0, 300, 1.0, 2.0])

#plt.plot(timearray, CL, '-', color='k', linewidth=2.0, markersize=4.0)
#plt.ylabel('CL',fontsize=14)
#plt.axis([0, 300,-0.4, 0.4])

plt.xlabel('Time',fontsize=14)


plt.grid('on')
plt.tight_layout()
plt.show()

plt.savefig('graph.png', dpi=1000)


