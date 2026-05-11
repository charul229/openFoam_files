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
U   = 1.1 # reference velocity
mu  = 0.01 # dynamic viscosity

factor = 0.5*rho*A*U**2

CD = Fx/factor
CL = Fy/factor



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
    fv = frq[ind]
    print("\n Vortex shedding frequency (fv) =  %.4f" % fv, " Hz \n")
    St = fv*D/U
    print("\n Strouhal number (St=fv*D/U) =  %.4f" % St, " Hz \n")
    plot(frq, np.abs(Y),'r') # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')
    xlim(0,1.0)
    grid('on')


sampling=1.0/(timearray[1]-timearray[0])

subplot(2,1,1)
plot(timearray, CL, 'k-', linewidth=2.0, markersize=8.0)
xlim(50.0,300)
ylim(-0.4,0.4)
#axis([0, 10.0, 0.0, 1.0])
xlabel('Time')
ylabel('CL')
grid('on')
subplot(2,1,2)
plotSpectrum(CL, sampling)
show()

savefig('powerspectrum.png', dpi=1000)


