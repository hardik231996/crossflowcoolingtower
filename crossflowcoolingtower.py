# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import scipy
from matplotlib import pyplot as plt
import pandas as pd
data=pd.read_excel("crossflowcoolingtower.xlsx","Sheet1")
print data
cost=scipy.array(data["Value"])
mw=cost[0]
mg=cost[1]
p=cost[2]#mm hg
twi=cost[3]#water inlet temperature
tgi=cost[4]#air inlet temperature
rh=cost[5]#relative humidity
def pp(t):
    psat=18.1016-(3644.0/(t+273.16-44.12))    #past function
    return psat
l=cost[6]
b=cost[7]
tw=np.zeros((101,101))
tg=np.zeros((101,101))
w=np.zeros((101,101))
dwdx=np.zeros((101,101))
dwdz=np.zeros((101,101))
ga=np.zeros((101,101))
gw=np.zeros((101,101))
twtz=np.zeros((101,101))
tw=np.zeros((101,101))
wsw=np.zeros((101,101))

hd=cost[8]#mass transfer coefficient
af=cost[9]#area per unit volume
dx=b/100
dz=l/100
ga=mg/100
for i in range(101):
    tw[i,0]=35.0#as at inlet 
for i in range(101):
    gw[i,0]=mw/100
    for j in range(101):
        tg[i,j]=23.0
        

hcr=(mw*4.18)/(mg*1.008)#heat capicities ratio
pp0=0.01*rh*pp(tg[0,0])#partial pressure
w[0,0]=(pp0/(760-pp0))*(18/28.4)#humidity at inlet

for j in range(100):
    for i in range(100):
        wsw[i,j]=(pp(tg[i,j])/(760.0-pp(tg[i,j])))*(18.0/28.4)
        dwdx[i,j]=ga*hd*af*(wsw[i,j]-w[i,j])
    
        w[i+1,j]=w[i,j]+dx*dwdx[i,j]
        gw[i,j+1]=gw[i,j]-ga*dwdx[i,j]*dz
        tw[i,j+1]=tw[i,j]-((tw[i,j]*ga*dwdx[i,j])/gw[i,j])
        tg[i+1,j]=-(hcr*(tw[i,j+1]-tw[i,j]))+tg[i,j]
        
print 'inlet temperature of water',twi
print 'inlet flowrate of water',mw  
print 'inlet temperature of air',tgi      
twater=np.transpose(tw)  
print 'out let temperature of water',tw[i,j+1]
gwo=100*gw[99,99]
print 'outlet temperature of air',tg[99,99]
print 'water flow rate out let',gwo
ee=plt.imshow(twater)
plt.show()
#as it is shown as we go down temp decreases howeveras we go from 
#left to right cooling is less as shown in red plot"

     
            
        
        
            
        
    
    
