import math as m
import numpy as n
import matplotlib.pyplot as l

def Traj (H,V,ang,X,Y):
    
    if Y==0:
        print("Error variable Y cannot be zero")
        return

    rad= m.radians(ang)
    Vx = V*m.cos(rad)
    Vy = V*m.sin(rad)
    s = m.sqrt(pow(Vy,2) - 4*(0.5*Y)*H)
    t1 = (-Vy + s )
    t1 = t1/Y
    t2= (-Vy - s )
    t2 = t2/Y
    
    if t1 <= 0:
        t1 = t2
        lin = n.linspace(0,t1)
        x = Vx*lin + 1/2*X*pow(lin,2)
        y = Vy*n.linspace(0,t1) + 1/2*Y*pow(lin,2)
    else:
        x = Vx*pow(lin,2) + 1/2*X*pow(lin,2)
        y = Vy*pow(lin,2) + 1/2*Y*pow(lin,2)
    l.plot(x,y,'khaki',label='My chances of failing')
    l.title('Rectilinear Motion')
    l.xlabel('Trajectory in X',color='b')
    l.ylabel('Trajectory in Y ',color='r')
    l.grid(True,color='darkgoldenrod')
    l.legend()
    l.show()