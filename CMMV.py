import numpy as np
p1=np.array([float(1.232),float(1.232),float(1.232)])
p2=np.array([float(1),float(1),float(1)])
p3=np.array([float(1.232),float(1.232)])
p4=np.array([float(1),float(1)])
p5=np.array([float(1.232)])
p6=np.array([float(1),float(1)])
p7=np.array([float(2),float(2)])
p8=np.array([float(3),float(3)])
p9=np.array([float(4),float(4)])
ang=30

def distance(p1,p2):
    e=0
    res=[]
    for p1[0] in p1: 
        r=(p1[e]-p2[e])**2 
        res.append(r)
    r=(sum(res[0:]))**(2**-1)
    return r
#distance(p1,p6)

def vector(p1,p2):
    e=0
    res=[]
    for p1[0] in p1: 
        r=(p2[e]-p1[e])
        res.append(r)
    return(np.array(res))

def vector_modulus(v1):
    e=0
    res=[]
    for v1[0] in v1:
        r=v1[e]**2
        res.append(r)
    r=sum(res[0:])**(2**-1)
    return(r)

#vector_modulus(p7)

def unit_vector():
    x=1

###############
def vector_product(v1,v2,ang):
    #print(v1,v2,ang)
    t=((3)**2**-1)
    print(2,t,ang)
    print((ang*np.pi)/180)
    #print(ang*(np.pi/180))
    print(2*t*ang)
    
    #return(np.array(r))

"""def vector_product(v1,v2):
    r=vector_modulus(v1)*vector_modulus(v2)
    print(np.array(r))
    return(np.array(r))"""

vector_product(vector_modulus(vector(p6,p7)),vector_modulus(vector(p8,p9)),30)

#print(np.sin(90*np.pi*1/180))