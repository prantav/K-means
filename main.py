import numpy as np



def centroidstarter(n):
  centroid_xpositions = np.random.uniform(size = n, 30,40)
  centroid_ypositions = np.random.uniform(size = n,30,40)
  centroid_position = {centroid_xpositions[i]:centroid_ypositions[i] for i in centroid_xpositions}
  return centroid_xpositions,centroid_ypositions,centroid_position

def dist(x1,x2,y1,y2):
  d = (x2-x1)**2+(y2-y1)**2
  return abs(d**(1/2))

def dictcreator(n):
  splitdict = {}
  for i in range(n):
    string = str("Centroid"+str(i))
    splitdict[string] = []
  return splitdict
    
def centroidmover(centroid_xpositions,centroid_ypositions,n,datax,datay,dictionary): 
  
  for i in range(len(datax)):
    xcoord = datax[i]
    ycoord = datay[i]
    splitting = dictionary
    for j in range(n):    
      for k in range(n):
        if dist(xcoord,ycoord,centroid_xpositions[k],centroid_ypositions[k])<= dist(xcoord,ycoord,centroid_xpositions[j],centroid_ypositions[j]):
            

  







