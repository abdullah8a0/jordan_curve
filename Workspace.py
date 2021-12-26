import numpy as np
import matplotlib.pyplot as plt

PERCISION = 0.1
M90 = np.array([[0,-1],[1,0]])

def R(polygon,pivot):
    return (pivot + polygon)/2 + np.matmul(((polygon - pivot)/2),M90)

def R_p(polygon,pivot):
    return (pivot + polygon)/2 + np.matmul(((polygon - pivot)/2),-M90) 

def isinside(polygon,point):    # TODO: parrallelize
    """
    If we draw a ray from point, parrallel to the x-axis, then point is
    inside polygon iff the number of interesections with the polygon boundary is odd.
    Ignoring edge effects ofcourse, but these cases are insignificant
    """
    x,y = point
    inside = sum( y1>=y>y2 or y2>y>=y1 for x1,y1,x2,y2 in np.concatenate((polygon,np.roll(polygon,1,axis=0)),axis=1) if x1>=x or x2>=x)%2 == 1
    return inside

def sigma1(p,polygon):
    rot1 = R(polygon,p)
    arr = [isinside(polygon,point) for point in rot1]
    res = [i for i in range(1,len(arr)) if arr[i]!= arr[i-1]]
    return res
def sigma2(p,polygon):
    rot2 = R_p(polygon,p)


def mobius_plot():
    pass

def populate(polygon,iter): # TODO: parrallelize
    new_poly = []
    for v1,v2 in zip(polygon,np.roll(polygon,1,axis=0)):
        t = [i/iter for i in range(iter)]
        new_poly.append(np.array([v1*(1-t_) + v2*t_ for t_ in t]))

    return np.concatenate(new_poly)

if __name__ == '__main__':
    boundary = np.array([[0,0],[0,-3],[-2,-2],[-3,0]])
    boundary = populate(boundary,100)
    rot = R(boundary,np.array([0,0]))
    Px = boundary[:,0]
    Py = boundary[:,1]
    ins = sigma1([0,0],boundary)
    plt.scatter(Px,Py,s=2)
    labels = np.ones(400)
    labels[ins] = 0
    plt.scatter(rot[:,0],rot[:,1],s=2,c=labels)
    #p = -3*np.random.rand(500,2)
    #plt.scatter(p[:,0],p[:,1],c=[isinside(boundary,i) for i in p],s=0.5)
    plt.axis("scaled")
    plt.show()