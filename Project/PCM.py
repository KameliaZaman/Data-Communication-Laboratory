import matplotlib.pyplot as plot
import numpy as np

A=2
fm=3
n=3

t=np.arange(0,1,1/(100*fm))
x=A*np.sin(2*np.pi*fm*t)      #Message signal

#Sampling
fs=20           #Sampling frequency/rate
ts=np.arange(0,1,1/fs)     #Sampling period/time
xs=A*np.sin(2*np.pi*fm*ts)

#Quantization
x1=xs+A
x1=x1/(2*A)
L=(-1+pow(2,n))
x1=L*x1
xq=np.round(x1)
#r=xq/L
#r=2*A*r
#r=r-A

#Encoding
y=[]
for i in range(len(xq)):
    d=np.binary_repr(int(xq[i]),n)
    d=float(d)-48
    y.append(d)

plot.subplot(3,3,1)
plot.plot(t,x)
plot.stem(ts,xs,use_line_collection=True)
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Sampled signal')
plot.grid(True)
#plot.show()

plot.subplot(3,3,2)
plot.stem(ts,x1,use_line_collection=True)
plot.stem(ts,xq,use_line_collection=True)
plot.plot(ts,xq)
plot.plot(t,(x+A)*L/(2*A))
plot.xlabel('Time')
plot.ylabel('Levels')
plot.title('Quantized signal')
plot.grid(True)
#plot.show()


plot.subplot(3,3,3)
plot.step(ts,y)
#plot.plot(ts,y)
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('PCM signal')
plot.grid(True)
#plot.axis([0,len(y),-1,2])
plot.show()

