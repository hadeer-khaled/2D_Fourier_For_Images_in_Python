# gratings.py

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-500, 501, 1)

X, Y = np.meshgrid(x, x)

wavelength = 100
angle = np.pi/9
grating = np.sin(
    2*np.pi*(X*np.cos(angle) + Y*np.sin(angle)) / wavelength
)

plt.set_cmap("gray")

plt.subplot(121)
plt.imshow(grating)

# Calculate Fourier transform of grating
ft = np.fft.ifftshift(grating)
ft = np.fft.fft2(ft) #The result of the FFT is an array of complex numbers.
ft = np.fft.fftshift(ft)

plt.subplot(122)
plt.imshow(abs(ft)) 
plt.xlim([480, 520])
plt.ylim([520, 480])  # Note, order is reversed for y
plt.show()


#The distance of the dots from the centre 
# represents the frequency of the sinusoidal grating.

#The orientation of the dots represents the orientation of the grating.
