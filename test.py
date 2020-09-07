#!/usr/bin/env python
# coding: utf-8

# In[3]:


from funciones import *
import numpy as np


# In[7]:


#1)
n=int(input('Ingrese el valor de n:'))
if (Factorial(n)==np.math.factorial(n)):
    print('La función es correcta')
    


# In[8]:


#2)
if Binomial(7,6)==7.0:
    print('El coeficiente binomial es correcto')

