# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:33:32 2020

@author: Mohith Sai
"""
""" Let us consider a slab with thickness of L with heat generation Qg
and T1 & T2 be the temperatures of the both ends respectively K thermal conductivity of the material
 the temperature distributuion over a slab is given by 
 T(x) = -(Qg/2*k)*x**2 + (T2-T1)*x/L + Qg*L*x/2*k + T1 """

import numpy as np
import matplotlib.pyplot as plt

T1 = 1000 #the temperature on first end and units must be degC
T2 = 10 #the temperature on first end and units must be degC
L = 1 #the length of the slab units must be in meters
Qg = 10 #heat generation units must be in W/m**3
K = 1000 #thermal conductivity units must be in W/m*k
n = 20 #the number of points
x = np.linspace(0, L, n) #linearlyspaced points
T = np.ones(n) #preallocating array of ones for temperature
const = Qg/(2*K) #creating a const variable which refers to value of Qg/2*k
for i in range(0, n) :
    T[i] = -(const*x[i]**2) + ((T2-T1)*x[i])/L + const*L*x[i] + T1 #temperature distribution
plt.figure(1)
plt.plot(x,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Graph')
print("The temperatures are:",T)
"""If you want to see parabolic curve set the T1=T2 or 
set the T1 and T2 with minimal difference with more heat generation"""
