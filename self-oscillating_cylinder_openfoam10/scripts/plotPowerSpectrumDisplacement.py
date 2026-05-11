import matplotlib.pyplot as plt
import numpy as np
from pylab import *

params = {'axes.labelsize': 14,
     'legend.fontsize': 14,
     'xtick.labelsize': 14,
     'ytick.labelsize': 14}
     
rcParams.update(params)     


filename='../postProcessing/sixDoFRigidBodyState/0/sixDoFRigidBodyState.dat'


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

#timearray = timearray[::10]
#liftforce = liftforce[::10]

def plotSpectrum(y,Fs):
 """
 Plots a Single-Sided Amplitude Spectrum of y(t)
 """
 n = len(y) # length of the signal
 k = arange(n)
 T = n/Fs
 frq = k/T # two sides frequency range
 frq = frq[range(int(n/2))] # one side frequency range

 Y = fft(y)/n # fft computing and normalization
 Y = Y[range(int(n/2))]
 ind = np.argmax(Y)
 print( " Frequency =  %.4f" % frq[ind], " Hz")
 plot(frq, np.abs(Y),'r') # plotting the spectrum
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')
 xlim(0,2.0)
 grid('on')



sampling=1.0/(timearray[1]-timearray[0])

subplot(2,1,1)
plot(timearray, dispY, 'k-', linewidth=2.0, markersize=8.0)
#ylim(0,2.0)
#axis([0, 10.0, 0.0, 1.0])
xlabel('Time')
ylabel('Amplitude')
grid('on')
subplot(2,1,2)
plotSpectrum(dispY, sampling)
show()

savefig('powerspectrum.png', dpi=1000)


