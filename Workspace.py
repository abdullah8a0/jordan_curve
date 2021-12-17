import numpy as np
import matplotlib.pyplot as plt

PERCISION = 0.1
M90 = np.array([[0,-1],[1,0]])

def R(polygon,pivot):
    print((polygon - pivot)/2)
    return (pivot + polygon)/2 + np.matmul(((polygon - pivot)/2),M90)


def isinside(polygon,point):    # parrallelize
    x,y = point
    inside = sum( y1>=y>=y2 or y2>=y>=y1 for x1,y1,x2,y2 in np.concatenate((polygon,np.roll(polygon,1)),axis=1) if x1>=x or x2>=x)%2 == 1
    return inside

def mobius_plot():
    pass

if __name__ == '__main__':
    boundary = np.array([[1,1],[1,-2],[-1,-1],[-1,1]])

    print(boundary)
    rot = R(boundary,np.array([1,1]))
    Px = boundary[:,0]
    Py = boundary[:,1]
    plt.plot(Px,Py,"ro")
    plt.plot(rot[:,0],rot[:,1],"bo")
    plt.axis("scaled")
    plt.show()