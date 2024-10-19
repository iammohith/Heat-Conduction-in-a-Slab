# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:33:32 2020

@author: Mohith Sai
"""

# This program calculates the temperature distribution across a slab of thickness L, 
# with heat generation (Qg) and known temperatures (T1 and T2) at both ends. 
# The material has a thermal conductivity K.
# The temperature distribution is given by the equation:
# T(x) = -(Qg/2*K)*x**2 + (T2-T1)*x/L + (Qg*L*x)/(2*K) + T1

import numpy as np
import matplotlib.pyplot as plt

# Defining the temperatures at both ends of the slab (in degrees Celsius)
T1 = 1000  # Temperature at one end of the slab (degC)
T2 = 10    # Temperature at the other end of the slab (degC)

# Defining the thickness of the slab (in meters)
L = 1  # Length of the slab (m)

# Heat generation rate (in W/m^3)
Qg = 10  # Heat generation per unit volume (W/m^3)

# Thermal conductivity of the slab material (in W/m*K)
K = 1000  # Thermal conductivity (W/m*K)

# Number of points along the slab to compute the temperature
n = 20  # Number of points

# Generate n linearly spaced points between 0 and L
x = np.linspace(0, L, n)

# Preallocate an array for the temperature values
T = np.ones(n)

# Constant term for Qg/(2*K), used in the temperature distribution equation
const = Qg / (2 * K)

# Calculate temperature distribution across the slab
for i in range(n):
    T[i] = -(const * x[i]**2) + ((T2 - T1) * x[i]) / L + (const * L * x[i]) + T1

# Plotting the temperature distribution
plt.figure(1)
plt.plot(x, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')

# Adding labels and title to the plot
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution Across the Slab')

# Display the calculated temperature values
print("The temperature values at each point are:", T)

# Show the plot
plt.show()

# Additional Note:
# If you want to see a parabolic curve in the temperature distribution, 
# set T1 = T2 or choose values of T1 and T2 that are very close with higher heat generation (Qg).
