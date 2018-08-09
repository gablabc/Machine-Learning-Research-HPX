#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 19:55:38 2018

@author: gabriel
"""


# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

### Reading data file ###
filename="rel_variances.txt"

Xdata=[]
variances=[]
Ydata=[]
with open(filename,"r") as file:
    n_experiments,n_features,n_targets=[int(j) for j in file.readline().split()]
    targets=np.array([float(j) for j in file.readline().split()[n_features:n_features+n_targets]])
    for i in range(n_experiments):
        line=file.readline().split()
        Xdata.append([float(j) for j in line[0:n_features]])
        variances.append([float(j) for j in line[n_features:]])


### Generate data arrays ###
Xdata=np.array(Xdata)
#Replace the execution times for unvalid chunk_size by 100
variances=np.array(variances)

Ydata=targets[np.where(variances==np.min(variances,axis=1).reshape((-1,1)))[1]]
plt.figure(1)
#%%
plt.plot(np.array([10,25,50,75,100]),variances[20:25,0],'r')
plt.plot(np.array([10,25,50,75,100]),variances[20:25,1],'g')
plt.plot(np.array([10,25,50,75,100]),variances[20:25,2],'b')
plt.plot(np.array([10,25,50,75,100]),variances[20:25,3],'k')
plt.yscale('log')
plt.xlabel('Number of repetition')
plt.ylabel('Relative variance of the mean time (%)')
plt.legend(['chunk-size=0.01','chunk-size=0.05','chunk-size=0.1','chunk-size=0.5'])
