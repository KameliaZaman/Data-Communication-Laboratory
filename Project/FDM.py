import matplotlib.pylab as plot
import numpy as np
from scipy import signal

fs=2000                         #Sampling rate
t=np.arange(0,1,1/fs)
mu=0
sigma=10
y=np.random.lognormal(mu,sigma)

Am1=2
fm1=4
m1=Am1*np.cos(2*np.pi*fm1*t)
#m1=m1+y

Am2=2
fm2=5
m2=Am2*np.cos(2*np.pi*fm2*t)

Am3=2
fm3=6
m3=Am3*np.cos(2*np.pi*fm3*t)

Ac1=2
fc1=25
c1=Ac1*np.cos(2*np.pi*fc1*t)

Ac2=2
fc2=50
c2=Ac2*np.cos(2*np.pi*fc2*t)

Ac3=2
fc3=75
c3=Ac3*np.cos(2*np.pi*fc3*t)

x=[]
for i in range(len(t)):
        x.append(m1[i]*c1[i]+m2[i]*c2[i]+m3[i]*c3[i])

plot.plot(t, x)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Composite Signal")
plot.grid(True)
plot.show()

[num1,den1]=signal.butter(5,[.5*(fc1-fm1)*4/fs,(fc1+fm1)*4/fs],'bandpass')
[num2,den2]=signal.butter(5,[.5*(fc2-fm2)*4/fs,(fc2+fm2)*4/fs],'bandpass')
[num3,den3]=signal.butter(5,[.5*(fc3-fm3)*4/fs,(fc3+fm3)*4/fs],'bandpass')
filtr1=signal.filtfilt(num1,den1,x)
filtr2=signal.filtfilt(num2,den2,x)
filtr3=signal.filtfilt(num3,den3,x)

lp1=[]
lp2=[]
lp3=[]
for i in range(len(t)):
        lp1.append(filtr1[i] * c1[i])
        lp2.append(filtr2[i] * c2[i])
        lp3.append(filtr3[i] * c3[i])

[num11,den11]=signal.butter(5,4*fm1/fs)
[num22,den22]=signal.butter(5,4*fm2/fs)
[num33,den33]=signal.butter(5,4*fm3/fs)
lpf_out1=signal.filtfilt(num11,den11,lp1)
lpf_out2=signal.filtfilt(num22,den22,lp2)
lpf_out3=signal.filtfilt(num33,den33,lp3)

plot.subplot(3,3,1)
plot.plot(t, m1)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Message Signal 1")
plot.grid(True)
#plot.show()

plot.subplot(3,3,2)
plot.plot(t, m2)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Message Signal 2")
plot.grid(True)
#plot.show()

plot.subplot(3,3,3)
plot.plot(t, m3)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Message Signal 3")
plot.grid(True)
#plot.show()

plot.subplot(3,3,4)
plot.plot(t, c1)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Carrier Signal 1")
plot.grid(True)
#plot.show()

plot.subplot(3,3,5)
plot.plot(t, c2)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Carrier Signal 2")
plot.grid(True)
#plot.show()

plot.subplot(3,3,6)
plot.plot(t, c3)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Carrier Signal 3")
plot.grid(True)
#plot.show()

plot.subplot(3,3,7)
plot.plot(t, lpf_out1)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Filter 1 output")
plot.grid(True)
#plot.show()

plot.subplot(3,3,8)
plot.plot(t, lpf_out2)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Filter 2 output")
plot.grid(True)
#plot.show()

plot.subplot(3,3,9)
plot.plot(t, lpf_out3)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("Filter 3 output")
plot.grid(True)
plot.show()