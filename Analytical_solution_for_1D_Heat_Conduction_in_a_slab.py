# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:06:58 2020

@author: Mohith Sai
"""
""" Let us consider a slab with thickness of L and T1 & T2 temperatures of both ends respectively
the temperature distributuion over a slab is given by T(x) = -(T1-T2)*x/L + T1 """

import numpy as np
import matplotlib.pyplot as plt

T1 = 1000 #the temperature on first end and units must be degC
T2 = 100 #the temperature on first end and units must be degC
L = 1 #the length of the slab units must be in meters
n = 20 #the number of points
x = np.linspace(0, L, n) #linearlyspaced points
T = np.ones(n) #preallocating array of ones for temperature
for i in range(0, n) :
    T[i] = -(((T1-T2)/L)*x[i])+T1 #temperature distribution
plt.figure(1)
plt.plot(x,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Graph')
if T1>T2:
    plt.axis([0, L , T2-1, T1+1])
elif T2>T1:
    plt.axis([0, L , T1-1, T2+1])
print("The temperatures are:",T)
