# gratings.py

import numpy as np
import matplotlib.pyplot as plt


fig, axs = plt.subplots(1,2) #axs is an array of axis

x = np.arange(-500, 501, 1)

X, Y = np.meshgrid(x, x)

wavelength = 200
grating = np.sin(2 * np.pi * X / wavelength)

plt.set_cmap("gray")
axs[0].imshow(grating)

# gratings.py

x_rotate = np.arange(-500, 501, 1)

X_rotate, Y_rotate = np.meshgrid(x_rotate, x_rotate)

wavelength_rotate = 200
angle_rotate = np.pi / 9
grating_rotate = np.sin(
    2*np.pi*(X_rotate*np.cos(angle_rotate) + Y_rotate*np.sin(angle_rotate)) / wavelength_rotate
)

plt.set_cmap("gray")
axs[1].imshow(grating_rotate)
plt.show()