#!/usr/bin/env python
# coding: utf-8

# In[1]:


from funciones import *


# In[2]:


#1
n= int(input('Ingrese un número:'))
fac= Factorial(n)
print('El factorial de', n, 'es:', fac)


# In[3]:


#2
n=int(input('Ingrese un número n:'))
k=int(input('Ingrese un k menor que n:'))
bino= Binomial(n,k)
print('El coeficiente binomial es:', bino)


# In[5]:


#3
n=int(input('Ingrese el valor de n:'))
print(Pascal(n))


# In[6]:


#4
#a)
print('La probabilidad de sacar cara 10 veces en un evento de 100 lanzamientos es:', Probabilidad(100,10))
#b)
for i in range(30):
    B=(1-Probabilidad(100,i))
print('La probabilidad de sacar cara más de 30 veces en un evento de 100 lanzamientos es',np.round(B,5))


# In[ ]:




