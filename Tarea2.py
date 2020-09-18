#!/usr/bin/env python
# coding: utf-8

# In[7]:


from vector import *
#pasando los vectores a coordenadas esféricas.
a=VectorCartesiano(1.5,.0,2.4)
b=VectorCartesiano(0.0,1.0,9.0)
c=VectorCartesiano(4.2,.05,.0)

c1=a.conv1()
print('a en coordenadas polares esféricas:',end='')
c1.Print()

c2=b.conv1()
print('b en coordenadas polares esféricas:', end='')
c2.Print()

c3=c.conv1()
print('c en coordenadas polares esféricas:',end='')
c3.Print()


# In[12]:


#productos internos
m1=np.round(a*b,2)
m2=np.round(c1*c2,2)
print('El producto interno de a con b, en coordenadas cartesianas es:', m1)
print('El producto interno de a con b, en coordenadas esféricas es:', m2)
m3=np.round(a*c,2)
m4=np.round(c1*c3,2)
print('El producto interno de a con c, en coordenadas cartesianas es:', m3)
print('El producto interno de a con c, en coordenadas esféricas es:', m4)
m5=np.round(b*c,2)
m6=np.round(c2*c3,2)
print('El producto interno de b con c, en coordenadas cartesianas es:', m5)
print('El producto interno de a con c, en coordenadas esféricas es:', m6)


# In[18]:


#Producto Cruz
v1=a.Cruz(b)
v2=c1.Cruz(c2)
print('El producto cruz de a con b, en coordenadas cartesianas es:', end='')
v1.Print()
print('El producto cruz de a con b, en coordenadas esféricas es:', end='')
v2.Print()
v3=a.Cruz(c)
v4=c1.Cruz(c3)
print('El producto cruz de a con c, en coordenadas cartesianas es:', end='')
v3.Print()
print('El producto cruz de a con c, en coordenadas esféricas es:', end='')
v4.Print()
v5=b.Cruz(c)
v6=c2.Cruz(c3)
print('El producto cruz de b con c, en coordenadas cartesianas es:', end='')
v5.Print()
print('El producto cruz de b con c, en coordenadas esféricas es:', end='')
v6.Print()


# In[29]:


#Angulo entre los vectores:

a1=np.round((a*b)/(a.mag*b.mag),4)
print('El ángulo entre a y b es:', a1)
a2=np.round((a*c)/(a.mag*c.mag),4)
print('El ángulo entre a y c es:', a2)
a3=np.round((b*c)/(b.mag*c.mag),4)
print('El ángulo entre b y c es:', a3)


# In[ ]:




