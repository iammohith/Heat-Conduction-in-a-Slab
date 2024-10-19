# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:06:58 2020

@author: Mohith Sai
"""

# This program calculates the temperature distribution across a slab of thickness L, 
# with known temperatures at both ends, T1 and T2. The distribution follows the equation:
# T(x) = -(T1-T2) * x / L + T1

import numpy as np
import matplotlib.pyplot as plt

# Defining the temperatures at both ends of the slab (in degrees Celsius)
T1 = 1000  # Temperature at one end of the slab (degC)
T2 = 100   # Temperature at the other end of the slab (degC)

# Defining the thickness of the slab (in meters)
L = 1  # Length of the slab (m)

# Number of points along the slab to compute the temperature
n = 20  # Number of points

# Generate n linearly spaced points between 0 and L
x = np.linspace(0, L, n)

# Preallocate an array for the temperature values
T = np.ones(n)

# Calculate temperature distribution across the slab
for i in range(0, n):
    T[i] = -(((T1 - T2) / L) * x[i]) + T1

# Plotting the temperature distribution
plt.figure(1)
plt.plot(x, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')

# Adding labels and title to the plot
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution Across the Slab')

# Setting the axes limits based on the temperature range
if T1 > T2:
    plt.axis([0, L, T2 - 1, T1 + 1])
else:
    plt.axis([0, L, T1 - 1, T2 + 1])

# Display the calculated temperature values
print("The temperature values at each point are:", T)

# Show the plot
plt.show()
