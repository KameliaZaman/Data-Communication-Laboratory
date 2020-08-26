import matplotlib.pylab as plot
import numpy as np

#F1 = int(input('Enter the frequency of 1st carrier='))
#F2 = int(input('Enter the frequency of 2nd carrier='))
F1=14
F2=6

amplitude = 5
time = np.arange(0, 1, 0.001)
x1 = amplitude * np.sin(2 * np.pi * F1 * time)  # 1st Carrier Signal
x2 = amplitude * np.sin(2 * np.pi * F2 * time)  # 2nd Carrier Signal

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

z = []  # Carrier signal modulated with binary wave
for i in range(len(time)):
    if y[i] == 0:
        z.append(amplitude * np.sin(2 * np.pi * F2 * time[i]))
    else:
        z.append(amplitude * np.sin(2 * np.pi * F1 * time[i]))

plot.subplot(3,3,1)
plot.plot(time, x1)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("1st Carrier Signal")
plot.grid(True)
#plot.show()

plot.subplot(3,3,2)
plot.plot(time, x2)
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.title("2nd Carrier Signal")
plot.grid(True)
#plot.show()

plot.subplot(3,3,3)
plot.plot(time, y)
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Binary input sequence signal')
plot.grid(True)
#plot.show()

plot.subplot(3,3,4)
plot.plot(time, z)
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title("Frequency Shift Keying Signal")
plot.grid(True)
plot.show()