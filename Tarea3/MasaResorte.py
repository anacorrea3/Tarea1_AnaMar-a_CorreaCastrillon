#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Oscilador:
    def __init__(self,y,t,w):
        self.y=np.array(y)
        self.t=t
        self.w=w
    
    def funcion(self,y,t):
        f= np.array([y[1],-(self.w**2)*y[0]])
        return f
    def solucion(self):
        sol= odeint(self.funcion,self.y,self.t)
        return sol

        
class OsciladorAmortiguado:
    def __init__(self,y,t,w,gamma):
        self.y=y
        self.t=t
        self.w=float(w)
        self.gamma=float(gamma)
    
    def fun(self,y,t):
        f= np.array([y[1],-((2*self.gamma)*y[1])-((self.w**2)*y[0])])
        return f
    
    def sol(self):
        sln= odeint(self.fun,self.y,self.t)
        return sln

