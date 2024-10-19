# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:09:49 2020

@author: Mohith Sai
"""

# This program calculates the temperature distribution across a slab of thickness L, 
# with heat generation (Qg). The temperatures at both ends of the slab are equal (T1).
# The temperature distribution is given by the equation:
# T(x) = 4 * (zeta - zeta**2) * (Tmax - T1) + T1
# Where Tmax = T1 + (Qg * L**2) / (8 * K) and zeta = x / L

import numpy as np
import matplotlib.pyplot as plt

# Defining the temperature at both ends of the slab (in degrees Celsius)
T1 = 120  # Temperature at both ends (degC)

# Defining the thickness of the slab (in meters)
L = 2  # Length of the slab (m)

# Heat generation rate (in W/m^3)
Qg = 10  # Heat generation per unit volume (W/m^3)

# Thermal conductivity of the slab material (in W/m*K)
K = 1000  # Thermal conductivity (W/m*K)

# Number of points along the slab to compute the temperature
n = 20  # Number of points

# Generate n linearly spaced points between 0 and L
x = np.linspace(0, L, n)

# Calculate Tmax (maximum temperature at the center of the slab)
Tmax = T1 + (Qg * L**2) / (8 * K)

# Preallocate arrays for temperature (T) and zeta
T = np.ones(n)  # Preallocate temperature array
zeta = np.ones(n)  # Preallocate zeta array (zeta = x / L)

# Calculate the temperature distribution across the slab
for i in range(n):
    zeta[i] = x[i] / L  # Calculate zeta for each point
    T[i] = (4 * (zeta[i] - zeta[i]**2)) * (Tmax - T1) + T1  # Temperature distribution

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
