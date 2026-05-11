import matplotlib.pyplot as plt
import numpy as np
from pylab import *

params = {'axes.labelsize': 14,
     'legend.fontsize': 14,
     'xtick.labelsize': 14,
     'ytick.labelsize': 14}
     
rcParams.update(params)     

filename='../postProcessing/sixDoFRigidBodyState/0/sixDoFRigidBodyState.dat'
#filename='../postProcessing1/sixDoFRigidBodyState/0/sixDoFRigidBodyState.dat'

with open(filename) as f:
    lines_after_3 = f.readlines()[3:]

#result1=[item.split("\n")[0] for item in lines_after_3]

timearray = np.zeros(shape(lines_after_3)[0])
dataarray = np.zeros( (shape(lines_after_3)[0],3) )

ind=0
for item in lines_after_3:
    result1 = item.split('\n')[0]
    #print(result1)
    result2 = result1.split('\t')
    #print(result2)
    timearray[ind] = float(result2[0])
    #
    result3=result2[1].replace('(','')
    result4=result3.replace(')','')
    dataarray[ind,:] = result4.split(' ')
    ind = ind+1

dispY = dataarray[:,1]

#plt.figure(2)
plt.plot(timearray, dispY, '-', color='k', linewidth=2.0, markersize=7.0)


plt.xlabel('Time',fontsize=14)
plt.ylabel('Displacement ',fontsize=14)

#plt.axis([0, 6, 0, 50])
plt.grid('on')

#plt.legend(loc='upper left', markerscale=1.0, ncol=1, handlelength = 2.2, numpoints=1, fontsize=12)
plt.tight_layout()

plt.show()
outfile = 'graph.png'
plt.savefig(outfile, dpi=1000)


