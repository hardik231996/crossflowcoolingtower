# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import scipy
mw=1.0
mg=3.0
p=760#mm hg
twi=35.0
tgi=23.0
rh=27.0
def pp(t):
    psat=18.1016-(3644.0/(t+273.16-44.12))    
    return psat
l=5.0
b=3.0
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

hd=4.1#mass transfer coefficient
af=2.0#area per unit volume
dx=3.0/100
dz=5.0/100
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
    
print 'out let temperature of water',tw[i,j+1]
gwo=100*gw[99,99]
print 'outlet temperature of air',tg[99,99]
print 'water flow rate out let',gwo

     
            
        
        
            
        
    
    