# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:22:22 2020

@author: Mohith Sai
"""

# This program calculates the temperature distribution across a slab with heat generation (Qg).
# Heat is transferred from both sides of the slab to a surrounding fluid at temperature Tinf.
# Both surfaces of the slab are assumed to be at the same temperature (Tw).
# The temperature distribution is given by:
# T(x) = Qg / (8*K) * (L**2 - 4*x**2) + Qg*L / (2*h) + Tinf
# Where 'h' is the heat transfer coefficient, and is calculated as:
# h = Qg * L / (2 * thetaW), with thetaW as the temperature difference between Tw and Tinf.

import numpy as np
import matplotlib.pyplot as plt

# Defining the wall temperature of both ends of the slab (in degrees Celsius)
Tw = 120  # Wall temperature (degC)

# Temperature of the surrounding fluid (in degrees Celsius)
Tinf = 35  # Fluid temperature (degC)

# Heat generation rate (in W/m^3)
Qg = 1000  # Heat generation per unit volume (W/m^3)

# Defining the thickness of the slab (in meters)
L = 2  # Length of the slab (m)

# Calculate the temperature difference (thetaW) between the wall and the surrounding fluid
if Tw > Tinf:
    thetaW = Tw - Tinf  # Tw is higher than Tinf
else:
    thetaW = Tinf - Tw  # Tinf is higher than Tw

# Convective heat transfer coefficient (in W/m^2*K)
h = (Qg * L) / (2 * thetaW)

# Thermal conductivity of the slab material (in W/m*K)
K = 1000  # Thermal conductivity (W/m*K)

# Number of points along half the slab to compute the temperature (symmetry from midplane)
n = 20  # Number of points

# Generate n linearly spaced points between 0 and L/2 (since the temperature is symmetric from the midplane)
x = np.linspace(0, L / 2, n)

# Preallocate an array for the temperature values
T = np.ones(n)

# Calculate temperature distribution across the slab (from midplane to one side)
for i in range(n):
    T[i] = (Qg / (8 * K)) * (L**2 - 4 * x[i]**2) + (Qg * L) / (2 * h) + Tinf

# Display the calculated temperature values
print("The temperatures from the midplane are:", T)

# Plotting the temperature distribution
plt.figure(1)
plt.plot(x, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')  # From midplane to right side
plt.plot(-x, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')  # Symmetry: from midplane to left side

# Adding labels and title to the plot
plt.xlabel('Distance from midplane (m)')
plt.ylabel('Temperature (°C)')
plt.title('Axisymmetrical Temperature Distribution')

# Show the plot
plt.show()
