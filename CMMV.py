import numpy as np
p1=np.array([float(1.2),float(1.2),float(1.2)])
p2=np.array([float(-1.2),float(1.3),float(1.3)])
p3=np.array([float(1.232),float(1.232),float(1.232)])
p4=np.array([float(1),float(-1),float(2)])
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
    r=(p2-p1)
    return(r)

def vector_modulus(v1):
    e=0
    res=[]
    for v1[0] in v1:
        r=v1[e]**2
        res.append(r)
    r=sum(res[0:])**(2**-1)
    return(r)

def unit_vector():
    x=1

###############

def vector_product(v1,v2):
    #print(v1,v2,ang)
    print(v1)
    r=1
    print(r)
    return(r) 
    
def unknown_function(v1,v2,ang):
    #print(v1,v2,ang)
    r=vector_modulus(v1)*vector_modulus(v2)*np.sin(ang*np.pi/180)
    print(r)
    return(r) 

#print(np.sin(ang*np.pi/180))
#vector_product((vector(p1 ,p2)),(vector(p1,p2)))

#print(np.sin(90*np.pi*1/180))