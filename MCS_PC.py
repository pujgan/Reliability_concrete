# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:37:26 2022

@author: pujitha
"""

### v1 : March 6, 2021
### Library Setup
import numpy as np
np.random.seed(0)
### Input data
n = 50000 # number of Monte-Carlo Simulation
P_factors = [0.5,0.6,0.7,0.8]
data_28 = [[51.73,5],[13.54,0.41],[118.83,6.86],[1309.86,15.02]] # fcm(MPa), flexure (kN), split tensile (kN), compression (kN)

L_beam = 400 # in mm
b_beam = 100 # in mm
D_beam = 100 # in mm
L_cyl = 200 # in mm
D_cyl = 100 # in mm

### Simple Random Sampling for Monte Carlo Simulations
fcm_28 = np.random.normal(data_28[0][0], data_28[0][1], n)
flex_28 = 1000*np.random.normal(data_28[1][0], data_28[1][1], n) # in N
spte_28 = 1000*np.random.normal(data_28[2][0], data_28[2][1], n) # in N
comp_28 = 1000*np.random.normal(data_28[3][0], data_28[3][1], n) # in N


### Reliability Analysis
resistance_F_28 = 0.7*np.sqrt(fcm_28)
resistance_T_28 = 0.1*fcm_28
resistance_C_28 = fcm_28
stress_F_28 = ((1.5*L_beam*flex_28)/(b_beam*D_beam*D_beam))
stress_T_28 = ((1.5*2*spte_28)/(np.pi*L_cyl*D_cyl))
stress_C_28 = (comp_28/(150*150))

res_28 = 2*np.ones((len(P_factors),4))

q = 0
for p_fac in P_factors:
 RF_F_28 = resistance_F_28 - p_fac*stress_F_28
 RF_T_28 = resistance_T_28 - p_fac*stress_T_28
 RF_C_28 = resistance_C_28 - p_fac*stress_C_28
 #print(np.amin(RF_M_28), np.amin(RF_T_28), np.amin(RF_C_28))
  
 res_28[q,0] = p_fac
 
 res_28[q,1:] = (1/n)*np.array([len(np.where(RF_F_28 < 0)[0]),len(np.where(RF_T_28 < 0)[0]),len(np.where(RF_C_28 < 0)[0])])
 q += 1
np.savetxt('res28.txt', res_28, delimiter=',')

print("res_28:\n",res_28)
