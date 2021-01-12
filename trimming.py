#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:38:34 2020

@author: apple
"""
from astropy.io import fits
import numpy as np

pathacer="C:/Users/Panda/Desktop/A1/mosaic.fits"
hdu_list=fits.open(pathacer)

data=hdu_list[0].data
hdu_list.close()
#bright star in the middle
mean = 0


r=355
for x in range(1075,1785):
    for y in range(int(-np.sqrt(r**2-(x-1430)**2))+3202,int(np.sqrt(r**2-(x-1430)**2))+3202):
        data[y,x]=mean

#upper bleeding
#trapezoid:
#        A       B
    
    
#    D              C
#slopeAD=(yA-yD)/(xA-xD); intercept=(xAyD-xDyA)/(xA-xD)
# A:1431,4608; B:1437,4608; C:1450,3387; D:1426,3387
slopeAD=(4608-3387)/(1431-1426)
interceptAD=(1431*3387-1426*4608)/(1431-1426)
for x in range(1426,1431):
    for y in range(3387,int(slopeAD*x+interceptAD)):
        data[y,x]=mean
slopeBC=(4608-3387)/(1437-1450)
interceptBC=(1437*3387-1450*4608)/(1437-1450)
for x in range(1437,1450):
    for y in range(3387,int(slopeBC*x+interceptBC)):
        data[y,x]=mean
for x in range(1431,1438):
    for y in range(3387,4607):
        data[y,x]=mean
       
for x in range(1038,1040):
    for y in range(4419,4424):
        data[y,x]=mean   
#down bleeding
xA=1425
yA=2850
xB=1451
yB=2850
xC=1449
yC=473
xD=1428
yD=473
#slopeAD=(yA-yD)/(xA-xD)
#interceptAD=(xA*yD-xD*yA)/(xA-xD)
#slopeADd = (2850-473)/(1425-1428)
#interceptADd = (1425*473-1428*2850)/(1425-1428)
#for x in range(1425,1428):
  #  for y in range(473,int(slopeADd*x+interceptADd)):
 #       data[y,x]=0
#slopeBC=(yB-yC)/(xB-xC)
#interceptBC=(xB*yC-xC*yB)/(xB-xC)
#slopeBCd=(2850-473)/(1428-1451)
#interceptBCd=(1437*3387-1450*4608)/(1437-1450)
#for x in range(1449,1451):
#    for y in range(473,int(slopeBCd*x+interceptBCd)):
 #       data[y,x]=0
for x in range(1425,1451):
    for y in range(0,2850):
        data[y,x]=mean
        
#edges 
#left
for x in range(0,180):
    for y in range(0,4611):
        data[y,x]=mean
#right
for x in range(2470,2570):
    for y in range(0,4611):
        data[y,x]=mean
# top     
for x in range(0,2570):
    for y in range(4500,4611):
        data[y,x]=mean
# bottom
for x in range(0,2570):
    for y in range(0,115):
        data[y,x]=mean

#horizontal bleeding 
#considered as two triangles and one rectangle underneath
#left triangle        right triangle
#          A            D
#       B  C            E  F
#Rectangle below
#slopeL=(yA-yB)/(xA-xB)
#interceptL=(xA*yB-xB*yA)/(xA-xB)

#first left triangle A(1426,469) B(1102,426) C(1426,426)
slope1l=(469-426)/(1426-1102)
intercept1l=(1426*426-1102*469)/(1426-1102)        
for x in range(1102,1426):
    for y in range(426,int(slope1l*x+intercept1l)):
          data[y,x]=mean  
  #first right triangle   D(1451,468) E(1451,426) F(1652,426)     
slope1r=(469-426)/(1451-1652)
intercept1r=(1451*426-1652*469)/(1451-1652)        
for x in range(1451,1652):
    for y in range(426,int(slope1r*x+intercept1r)):
          data[y,x]=mean  
#first rectangle 
for x in range(1102,1652):
    for y in range(426,429):
          data[y,x]=mean        

#second rectangle     
for x in range(1018,1703):
    for y in range(314,319):
        data[y,x]=mean
  #second left triangle     A(1426,356) B(1018,314) C(1426,314) 
slope2l=(356-314)/(1426-1018)
intercept2l=(1426*314-1018*356)/(1426-1018)        
for x in range(1018,1426):
    for y in range(314,int(slope2l*x+intercept2l)):
          data[y,x]=mean  
   #second right triangle     D(1451,369) E(1451,314) F(1736,314)        
slope2r=(369-314)/(1451-1703)
intercept2r=(1451*314-1703*369)/(1451-1703)        
for x in range(1451,1703):
    for y in range(314,int(slope2r*x+intercept2r)):
          data[y,x]=mean            

      #third left triangle A(1426,265) B(1385,231) C(1426,231)
slope3l=(265-231)/(1426-1385)
intercept3l=(1426*231-1385*265)/(1426-1385)        
for x in range(1385,1426):
    for y in range(231,int(slope3l*x+intercept3l)):
          data[y,x]=mean            
      #third right triangle    D(1451,258) E(1451,231) F(1482,231)
slope3r=(258-231)/(1451-1482)
intercept3r=(1451*231-1482*258)/(1451-1482)        
for x in range(1451,1482):
    for y in range(231,int(slope3r*x+intercept3r)):
          data[y,x]=mean            

#fourth left triangle       A(1426,241) B(1398,218) C(1426,218)
slope4l=(241-218)/(1426-1398)
intercept4l=(1426*218-1398*241)/(1426-1398)        
for x in range(1398,1426):
    for y in range(218,int(slope4l*x+intercept4l)):
          data[y,x]=mean   
#fourth right triangle  D(1451,236) E(1451,218) F(1471,218)
slope4r=(236-218)/(1451-1471)
intercept4r=(1451*218-1471*236)/(1451-1471)        
for x in range(1451,1471):
    for y in range(218,int(slope4r*x+intercept4r)):
          data[y,x]=mean        
for x in range(1397,1471):
    for y in range(218,219):
        data[y,x]=mean
   
#fifth left triangle        A(1426,162) B(1340,126) C(1426,126) 
slope5l=(162-126)/(1426-1340)
intercept5l=(1426*126-1340*162)/(1426-1340)        
for x in range(1340,1426):
    for y in range(126,int(slope5l*x+intercept5l)):
          data[y,x]=mean   
#fifth right triangle    D(1451,146) E(1451,126) F(1497,126)
slope5r=(146-126)/(1451-1497)
intercept5r=(1451*126-1497*146)/(1451-1497)        
for x in range(1451,1497):
    for y in range(126,int(slope5r*x+intercept5r)):
          data[y,x]=mean    
#big rectangle under fifth triangle          
for x in range(1390,1468):
    for y in range(117,122):
        data[y,x]=mean
#small rectangle under fifth triangle 
for x in range(1290,1524):
    for y in range(122,128):
        data[y,x]=mean
                                
#other bleeding stars
#bottom right around the horizontal bleeding area

for x in range(1526,1538):
    for y in range(117,124):
        data[y,x]=mean
for x in range(1530,1535):
    for y in range(124,138):
        data[y,x]=mean

for x in range(1641,1645):
    for y in range(333,344):
        data[y,x]=mean
for x in range(1645,1648):
    for y in range(334,336):
        data[y,x]=mean        
for x in range(1642,1645):
    for y in range(344,354):
        data[y,x]=mean        
 
        
#bleeding??? 
#for x in range(2085,2093):
#    for y in range(1402,1451):
#        data[y,x]=0              
#for x in range(2078,2100):
#    for y in range(1417,1436):
#        data[y,x]=0   
r=41
for x in range(2045,2127):
    for y in range(int(-np.sqrt(r**2-(x-2086)**2))+1416,int(np.sqrt(r**2-(x-2086)**2))+1416):
        data[y,x]=mean

         
#bleeding???   (2133,2310)      
r=35
for x in range(2098,2168):
    for y in range(int(-np.sqrt(r**2-(x-2133)**2))+2310,int(np.sqrt(r**2-(x-2133)**2))+2310):
        data[y,x]=mean
        
#topright corner
r=27
for x in range(2440,2494):
    for y in range(int(-np.sqrt(r**2-(x-2467)**2))+3415,int(np.sqrt(r**2-(x-2467)**2))+3415):
        data[y,x]=mean
for x in range(2465,2468):
    for y in range(3385,3440):
        data[y,x]=mean        

r=44
for x in range(2090,2179):
    for y in range(int(-np.sqrt(r**2-(x-2134)**2))+3760,int(np.sqrt(r**2-(x-2134)**2))+3760):
        data[y,x]=mean        
for x in range(2133,2135):
    for y in range(3706,3717):
        data[y,x]=mean        

r=32
for x in range(1425,1489):
    for y in range(int(-np.sqrt(r**2-(x-1457)**2))+4032,int(np.sqrt(r**2-(x-1457)**2))+4032):
        data[y,x]=mean  
for x in range(1467,1488):
    for y in range(4004,4017):
        data[y,x]=mean 
        
#bottom left around the horizontal bleeding area
for x in range(1027,1043):
    for y in range(426,429):
        data[y,x]=mean         
for x in range(1035,1039):
    for y in range(424,451):
        data[y,x]=mean         
                
r=55
for x in range(851,961):
    for y in range(int(-np.sqrt(r**2-(x-906)**2))+2286,int(np.sqrt(r**2-(x-906)**2))+2286):
        data[y,x]=mean         
for x in range(902,908):
    for y in range(2224,2356):
        data[y,x]=mean    

r=56
for x in range(918,1030):
    for y in range(int(-np.sqrt(r**2-(x-974)**2))+2774,int(np.sqrt(r**2-(x-974)**2))+2774):
        data[y,x]=mean  
for x in range(971,976):
    for y in range(2705,2834):
        data[y,x]=mean            


#top left
r=56
for x in range(720,832):
    for y in range(int(-np.sqrt(r**2-(x-776)**2))+3320,int(np.sqrt(r**2-(x-776)**2))+3320):
        data[y,x]=mean  
for x in range(772,778):
    for y in range(3204,3417):
        data[y,x]=mean   

r=30
for x in range(529,589):
    for y in range(int(-np.sqrt(r**2-(x-559)**2))+4097,int(np.sqrt(r**2-(x-559)**2))+4097):
        data[y,x]=mean    
        
        

        
hdu = fits.PrimaryHDU(data)
hdul = fits.HDUList([hdu])
hdul.writeto('trimmed10.fits')



