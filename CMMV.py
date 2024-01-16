import numpy as np
p1=np.array([float(1.232),float(1.232),float(1.232)])
p2=np.array([float(1),float(1),float(1)])
p3=np.array([float(1.232),float(1.232)])
p4=np.array([float(1),float(1)])
p5=np.array([float(1.232)])
p6=np.array([float(1),float(0),float(0)])

def distance(p1,p2):
    e=0
    res=[]
    for p1[0] in p1:
        r=(p1[e]-p2[e])**2
        res.append(r)
    r=(sum(res[0:]))**(2**-1)
    print(r)
    return r
distance(p1,p6)