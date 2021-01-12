# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:33:37 2020

@author: Panda
"""
from astropy.io import fits
import numpy as np
import math

#different paths for dif computers
pathic="//icnas2.cc.ic.ac.uk/ip1016/Desktop/LAB/A1/trimmed6.fits"
paththinkpad="C:/Users/User/Desktop/LAB A1/trimmed10mean.fits"
pathacer="C:/Users/Panda/Desktop/A1/trimmed10mean.fits"

#import the image
hdu_list=fits.open(pathacer)
data=hdu_list[0].data
hdu_list.close()
slice=data

mean=3418.71 #mean of he background
sigma=11.27 #std of the background
max=10000 #an initial value for the max to get the loop going
galaxies=[] #the catalogue
list_mag=[]
list_size=[]
count_of_errors=0
threshold_1=mean

#the loop which detects the galaxies
while max>mean+4*sigma: #verify if the maximum is above the threshold
    max=slice.max()
    max_arg=np.argmax(slice)+1
    max_row_y=max_arg//(slice.shape[1])+1-1
    max_col_x=max_arg%(slice.shape[1])-1
    m=max_row_y
    count=0
    counter_star=0
    count_back=0
    counter_back=0
    
    #calculating the parameters of the Bayesian method to determine the detection threshold for each galaxy
    aux=slice[max_row_y-30:max_row_y+30,max_col_x-30:max_col_x+30]
    NBINS=slice.max()-slice.min()
    hist=np.histogram(aux,NBINS)
    omega=0
    miu=0
    miu_T=0
    tr_list=[]
    tr_list_index=[]
   
    for k in range(0,len(hist[0])-1):
        miu_T=miu_T+hist[1][k]*hist[0][k]/np.sum(hist[0])
    for k in range(0,len(hist[0])-1):
        omega=omega+hist[0][k]/np.sum(hist[0])
        miu=miu+hist[1][k]*hist[0][k]/np.sum(hist[0])
        tr_list_index.append(k)
        sigma_b=(miu_T*omega-miu)**2//(omega*(1-omega))
        tr_list.append(sigma_b)
      
    sigma_b_max=np.amax(tr_list)
    sigma_b_max_arg=np.argmax(tr_list)
    threshold_2=hist[1][sigma_b_max_arg]
    
    if threshold_2<mean:
        threshold_2=mean
       
    
  #calculate the brightness of the deetcted galaxies in all four quarters 
  
    #right,down corner
    while slice[m,max_col_x]>threshold_1:
        l=max_col_x
        #print(l)
        while slice[m,l]>threshold_1:
            if slice[m,l]>threshold_2:
            #print(m,l,slice[m,l])
                count=count+slice[m,l]
                counter_star=counter_star+1
                count_back=count_back+slice[m,l]+slice[m,l+1]+slice[m,l+2] #nu iti numara si backgroundul de sus,Ioana
                counter_back=counter_back+3
            slice[m,l]=mean
            l=l+1
             
          
        
        m=m+1

    #right,up corner

    m=max_row_y-1
    while slice[m,max_col_x]>threshold_1:
        l=max_col_x
        while slice[m,l]>threshold_1:
            if slice[m,l]>threshold_2:
            #print(m,l,slice[m,l])
                count=count+slice[m,l]
                counter_star=counter_star+1
                count_back=count_back+slice[m,l]+slice[m,l+1]+slice[m,l+2] #nu iti numara si backgroundul de sus,Ioana
                counter_back=counter_back+3
            slice[m,l]=mean
            l=l+1
        
        m=m-1

    #left, down corner
    m=max_row_y
    while slice[m,max_col_x-1]>threshold_1:
        l=max_col_x-1
        while slice[m,l]>threshold_1:
            if slice[m,l]>threshold_2:
                count=count+slice[m,l]
                counter_star=counter_star+1 
                count_back=count_back+slice[m,l]+slice[m,l+1]+slice[m,l+2] #nu iti numara si backgroundul de sus,Ioana
                counter_back=counter_back+3
            slice[m,l]=mean
            l=l-1
        
        m=m+1

    #left,up corner
    m=max_row_y-1
    while slice[m,max_col_x-1]>threshold_1:
        l=max_col_x-1
        while slice[m,l]>threshold_1:
            if slice[m,l]>threshold_2:
                count=count+slice[m,l]
                counter_star=counter_star+1
                count_back=count_back+slice[m,l]+slice[m,l+1]+slice[m,l+2] #nu iti numara si backgroundul de sus,Ioana
                counter_back=counter_back+3
            slice[m,l]=mean
            l=l-1
        m=m-1
        
    count_back_avg=count_back/counter_back
    count_final=count-count_back_avg*counter_star
    if count_final>0:
        mag=-2.5*math.log10(count_final)+25.3
        list=[max_row_y,max_col_x,max,count,counter_star,count_back_avg,count_final,mag]
        galaxies.append(list)
        list_mag.append(mag)
        list_size.append(counter_star)
    else:
        mag=100
        count_of_errors=count_of_errors+1

min_mag=int(np.min(list_mag))
max_mag=int(np.max(list_mag))+1
mag_counts=[]
counter_mag=0
list_aux=[]
#count the galaxies brighter than a certain magnitude
for j in range(min_mag, max_mag):
    for i in range(0,len(list_mag)):
        if list_mag[i]<j:
            counter_mag=counter_mag+1
    list_aux=[j,counter_mag]
    mag_counts.append(list_aux)
    counter_mag=0
list_aux_size=[]
size_counts=[]
counter_size=0

#study the size of the galaxies
for j in range(int(np.min(list_size)),int(np.max(list_size)),10):
    for i in range(0,len(list_size)):
        if list_size[i]<100000:
            if list_size[i]>0:
                counter_size=counter_size+1
    list_aux_size=[j,j+10,counter_size]
    size_counts.append(list_aux_size)
    counter_size=0
print(mag_counts)    
import xlsxwriter

#export the data in an excel file
workbook = xlsxwriter.Workbook('galaxies_variable_boundaries.xlsx')
worksheet = workbook.add_worksheet()



row = 0
col = 0

for i in ['y center','x center','value center','initial count','star count','background count average','final count','mag']:
    worksheet.write(row, col,i)
    col=col+1
    
row=1
col=0

for i,j,k,l,m,n,o,p in galaxies:
    worksheet.write(row, col,i)
    worksheet.write(row, col+1,j)
    worksheet.write(row, col+2,k)
    worksheet.write(row, col+3,l)
    worksheet.write(row, col+4,m)
    worksheet.write(row, col+5,n)
    worksheet.write(row, col+6,o)
    worksheet.write(row, col+7,p)
    row += 1

row=0
for i,j in mag_counts:
    worksheet.write(row, col+10,i)
    worksheet.write(row, col+11,j)
    row+=1
    
row=0
for i,j,k in size_counts:
    worksheet.write(row, col+15,i)
    worksheet.write(row, col+16,j)
    worksheet.write(row, col+17,k)
    row+=1
workbook.close()
    