import math
import matplotlib.pyplot as plt

Percision = 0.1
Points = [[1,1],[1,-1],[-1,-1],[-1,1]]
Order = [[0,1],[1,2],[2,3],[3,0]]

def R(point,centerPoint,angle = 90):
    angle = math.radians(angle)
    temp_point = [point[0]-centerPoint[0] , point[1]-centerPoint[1]]
    temp_point = [temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle)]
    temp_point = [temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]]
    return temp_point

def mid(a, b):
    Ax, Ay = a[0], a[1]
    Bx, By = b[0], b[1]
    Cx = (Ax + Bx) / 2
    Cy = (Ay + By) / 2
    return [Cx, Cy]

def Sigma(p, q):
    return [S1(p, q), S2(p, q)]

def S1(p, q):
    m = mid(p, q)
    return R(p, m)

def S2(p, q):
    m = mid(p, q)
    return R(q, m)

def Slice():
    for index,i in enumerate(Points):
        bef = i
        aft = Points[(index + 1)%(len(Points)-1)]
        new = mid(bef, aft)
        Points.append(new)
    return
Slice()
print("Sliced")
Px = [Points[x][0] for x in range(len(Points))]
Py = [Points[y][1] for y in range(len(Points))]
print("Ordered")
plt.plot(Px,Py,"ro")
plt.show()
print(Points)