#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
class VectorCartesiano:
   def __init__(self, x, y,z):
       self.a=float(x)
       self.b=float(y)
       self.c=float(z)
       self.mag=(self.a**2+self.b**2+self.c**2)**0.5
   def __mul__(self, other):  
       '''Sobrecarga del operador * como producto interno'''
       return((self.a*other.a)+(self.b*other.b)+(self.c*other.c))
   def Cruz(self,other):
       '''Creación método producto cruz'''
       return VectorCartesiano(((self.b*other.c)-(self.c*other.b)),((self.c*other.a)-(self.a*other.c)),((self.a*other.b)-(self.b*other.a)))
   def __add__(self, other):
       '''Sobrecarga del operador +'''
       return VectorCartesiano(self.a + other.a, self.b + other.b, self.c + other.c)
   def __sub__(self, other):
       '''Sobrecarga del operador -'''
       return VectorCartesiano(self.a - other.a, self.b - other.b, self.c - other.c)
   def __getitem__(self,index):
       '''Sobrecarga del operador []'''
       self.q=([self.a,self.b,self.c])
       return self.q[index]
   def __eq__(self, other):
       '''Sobrecarga del operador =='''
       return (self.a==other.a and self.b==other.b and self.c==other.c)
   def conv1(self):
      
       
       rc=np.round(self.mag,4)
       if self.c>0:
           t=np.round(np.arctan(np.sqrt(self.a**2+self.b**2)/self.c),4)
       elif self.c==0:
           t=np.round(np.pi/2,4)
       else:
           t=np.round(np.pi + (np.arctan(np.sqrt(self.a**2+self.b**2)/self.c)),4)
                       
                       
       if (self.a>0) and (self.b>0):
           p=np.round(np.arctan(self.b/self.a),4)
       elif (self.a>0) and (self.b<0):
           p=np.round((2*np.pi)+np.arctan(self.b/self.a),4)
       elif self.a==0:
           p=np.round(np.pi/2,4)
       elif self.b==0:
           p=0.0
       elif self.a<0:
           p=np.round(np.pi+np.arctan(self.b/self.a),4)
       return VectorCartesiano(rc,t,p)
   def Print(self):
       '''Imprime el vector'''
       print(f"[{self.a},{self.b},{self.c}]") 


# In[29]:


import numpy as np
class VectorPolar(VectorCartesiano):
    def __init__(self,r,theta,phi):
        
        self.d=float(r)
        self.e=float(theta)
        self.f=float(phi)
        VectorCartesiano.__init__(self,self.d,self.e,self.f)
        
    def conv2(self):
        if self.d>=0 and (0<=self.e<np.pi) and (0<=self.f<2*np.pi):
            p=np.round(self.d*np.sin(self.e)*np.cos(self.f),2)
            q=np.round(self.d*np.sin(self.e)*np.sin(self.f),2)
            w=np.round(self.d*np.cos(self.e),2)
        return VectorCartesiano(p,q,w)
    
    def Print(self):
        '''Imprime el vector'''
        print(f"[{self.d},{self.e},{self.f}]")
        

