import pandas as pd
import numpy as np



def mwrd(directory='/Users/thoughtworker/chicago-river-sewage/data/', file='mwrd_rain_measurements.csv'):
   data= pd.read_csv(directory+file, na_values='na')
   print data.shape[0]
   location= list(set(data.ix[0:,3]))

   lat=['nan',41.824857, 42.079825, 41.821587, 41.734139, 41.659136, 41.894294, 41.912744, 41.721979, 42.075623, 41.970287, 42.019087, 41.735587]    
   lng=['nan',-87.655586, -87.821792, -87.773094, -87.782139, -87.612606, -87.625152, -87.723944, -87.548275, -87.685299, -87.701213, -87.716341, -87.682604]

   latitude,longitude={},{}
   for key, val in zip(location, lat):
       latitude[key]=val
   for key, val in zip(location,lng):
       longitude[key]= val
   print len(latitude), len(longitude) 

   coord=np.zeros(shape=(data.shape[0],2))
   ct=0
   for loc in data.ix[:,3]:
      coord[ct,0]=latitude[loc]
      coord[ct,1]=longitude[loc]
      ct+=1

   data_new=np.hstack((data.ix[:,:],coord))
   
   print data_new.shape
   np.savetxt(file, data_new,fmt='%s', delimiter=",")

def clean_water(directory='/Users/thoughtworker/chicago-river-sewage/data/',file='clean-waterway-measurements.csv'):
    data=pd.read_csv(directory+file, na_values='na')
    np.savetxt(file, data,fmt='%s', delimiter=",")

def cso():
   directory='/Users/thoughtworker/chicago-river-sewage/data/'
   cso_file='cso_events_timestamped.csv'
   
   cso_data= pd.read_csv(directory+cso_file, na_values='na')
   print cso_data.shape
          

if __name__=="__main__":
    mwrd()
    #cso()
    #clean_water()