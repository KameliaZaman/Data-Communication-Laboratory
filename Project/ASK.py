import matplotlib.pylab as plot
import numpy as np

#F1 = int(input('Enter the frequency of carrier='))
F1=9
amplitude = 3
time = np.arange(0, 1, 0.001)
x = amplitude * np.sin(2 * np.pi * F1 * time)  # Carrier Signal

y = []  # Binary Input Sequence Signal
phase = [0.2, 0.4, 0.6, 0.8, 1.0]
sign = 1
for i in time:
    if i == phase[0]:
        phase.pop(0)
        if sign == 0:
            sign = 1
        else:
            sign = 0
    y.append(sign)

z = []  # Carrier signal modulated with binary signal
for i in range(len(time)):
    z.append(amplitude * np.sin(2 * np.pi * F1 * time[i]) * y[i])

plot.subplot(3,3,1)
plot.plot(time, x)
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Carrier Signal')
plot.grid(True)
#plot.show()

plot.subplot(3,3,2)
plot.plot(time, y)
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Binary input sequence signal')
plot.grid(True)
#plot.show()

plot.subplot(3,3,3)
plot.plot(time, z)
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Amplitude Shift Keying Signal')
plot.grid(True)
plot.show()
