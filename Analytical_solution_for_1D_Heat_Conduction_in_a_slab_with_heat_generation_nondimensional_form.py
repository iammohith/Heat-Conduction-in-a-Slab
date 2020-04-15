# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:09:49 2020

@author: Mohith Sai
"""
"""Lets us consider a slab with thickness of L with heat generation Qg
and T1 & T2 be the temperatures of the both ends respectively adn they are equal to T1
K thermal conductivity of the material
the equation is T(x) = 4*(zeta - zeta**2)*(Tmax - T1) + T1
where Tmax = T1 + Qg*L**2/8*k zeta = x/L"""

import numpy as np
import matplotlib.pyplot as plt 

T1 = 120 #temperature at both ends are same  units must be degC
L = 2 #the length of the slab units must be in meters
Qg = 10 #heat generation units must be in W/m**3
K = 1000 #thermal conductivity units must be in W/m*k
n = 20 #the number of points
x = np.linspace(0, L, n) #linearlyspaced points
Tmax =  T1 + (Qg*L**2)/(8*K)
T = np.ones(n) #preallocating array of ones for temperature
zeta = np.ones(n) #preallocating array of ones for zeta
for i in range(0, n) :
    zeta[i] = x[i]/L
    T[i] = (4*(zeta[i] - zeta[i]**2))*(Tmax - T1) + T1 #temperature distribution
plt.figure(1)
plt.plot(x,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Graph')
print("The temperatures are:",T)