#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Punto 1
def Factorial(n):
    'Definiendo la función factorial para números enteros'
    n=int(n) #Números enteros únicamente
    if n>0: #Números enteros positivos
        x=Factorial(n-1)*n #Recursividad
    elif n==1 or n==0: 
        x=1
    else:
        x=print('Ingrese un número entero y positivo') #Números enteros negativos
    return x  


# In[14]:


#Punto 2
def Binomial(n,k):
    'Definición de la función binomial utilizando el factorial definido con anterioridad'
    if n==1 or n==k:
        b=1
    elif n>k:
        b= Factorial(n)/(Factorial(k)*Factorial(n-k))
    elif n<k:
        b=0
    return b


# In[12]:


#Punto 3
def Pascal(n):
    for line in range(n):
        for i in range(line+1):
            print(Binomial(line,i)," ",end= " ")
        print()


# In[ ]:


#Punto 4
import numpy as np
def Probabilidad(n,k):
    'Definición de la probabilidad de que cuando se lanza una moneda n veces salga cara k veces'
    p= np.round(Binomial(n,k)/(2**n),18) #Utilización de la función Binomial definida con anterioridad
    return p


# In[ ]:




