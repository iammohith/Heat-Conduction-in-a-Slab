# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:22:22 2020

@author: Mohith Sai
"""
""" Let us consider a slab with thickness of L with heat generation Qg
K thermal conductivity of the material
and let us consider the case where heat is transffered from two sides of wall
to surrounding fluid at Tinf for simplicity let us assume that 
temperature of both surafces are at Tw
the temperature distributuion over a slab is given by
 T(x) = Qg/8*k*(L**2 - 4*x**2) + Qg*L/2*h + Tinf 
 where h is heat transfer coefficient and at wall it is given by 
 h = Qg*L/2*(thetaW) thetaW is temperature difference"""

import numpy as np
import matplotlib.pyplot as plt

Tw = 120 #the wall temperature of the both ends units must be in degC
Tinf = 35 #the temperature of surrounding fluid units muts be in 
Qg = 1000 #heat generation units must be in W/m**3
L = 2 #the length of the slab units must be in meters
if Tw > Tinf : #if condition for Tw>Tinf
    thetaW = Tw - Tinf #temperature difference
elif Tinf > Tw : #if condition for Tinf>Tw
    thetaW = Tinf - Tw #temperature difference
h = (Qg*L)/(2*(thetaW)) #convective heat tranfer coeff
K = 1000 #thermal conductivity units must be in W/m*k
n = 20 #the number of points
x = np.linspace(0, L/2, n) #linearlyspaced points
T = np.ones(n) #preallocating array of ones for temperature
for i in range(0, n) :
    T[i] = ((Qg/(8*K))*(L**2 - 4*x[i]**2)) + ((Qg*L)/(2*h)) + Tinf
print("The temperatures from midplane are:",T)
plt.figure(1)
plt.plot(x,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.plot(-x,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce from mid plane (m)')
plt.ylabel('Temperature (C)')
plt.title('Axisyymetrical Temperature Graph')