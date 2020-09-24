#!/usr/bin/env python
# coding: utf-8

# In[1]:


from MasaResorte import *        


# In[2]:


t=np.arange(0,80,0.1)
y0=np.array([4,3])
y1=np.array([6,6])
y2=np.array([8,9])
y3=np.array([10,12])
y4=np.array([12,15])


v=Oscilador(y0,t,0.6)
v1=Oscilador(y1,t,0.9)
v2=Oscilador(y2,t,1.2)
v3=Oscilador(y3,t,1.5)
v4=Oscilador(y4,t,1.8)
b=v.solucion()
b1=v1.solucion()
b2=v2.solucion()
b3=v3.solucion()
b4=v4.solucion()

plt.figure(figsize=(20, 19))
plt.subplot(3,2,1)
plt.plot(t,b[:,0],label='y0',color='green')
plt.title('Solución caso 1')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,2)
plt.plot(t,b1[:,0],label='y1',color='red')
plt.title('Solución caso 2')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,3)
plt.plot(t,b2[:,0],label='y2',color='purple')
plt.title('Solución caso 3')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,4)
plt.plot(t,b3[:,0],label='y3',color='brown')
plt.title('Solución caso 4')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,5)
plt.plot(t,b4[:,0],label='y4',color='darkblue')
plt.title('Solución caso 5')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,6)
plt.plot(t,b[:,0],label='y0',color='green')
plt.plot(t,b1[:,0],label='y1',color='red')
plt.plot(t,b2[:,0],label='y2',color='purple')
plt.plot(t,b3[:,0],label='y3',color='brown')
plt.plot(t,b4[:,0],label='y4',color='darkblue')
plt.title('Todos los casos')
plt.xlabel('t(s)')
plt.ylabel('y(m)')
plt.legend()

plt.savefig('Oscilador.jpg')
plt.show()


# In[7]:


plt.figure(figsize=(20, 19))
plt.subplot(3,2,1)
plt.plot(b[:,0],b[:,1],color='green')
plt.title('Espacio de fase caso 1')
plt.xlabel('Posición(m)')
plt.ylabel("Velocidad(m/s)")


plt.subplot(3,2,2)
plt.plot(b1[:,0],b1[:,1],color='red')
plt.title('Espacio de fase caso 2')
plt.xlabel('Posición (m)')
plt.ylabel("Velocidad(m/s)")


plt.subplot(3,2,3)
plt.plot(b2[:,0],b2[:,1],color='purple')
plt.title('Espacio de fase caso 3')
plt.xlabel('Posición (m)')
plt.ylabel('Velocidad (m/s)')


plt.subplot(3,2,4)
plt.plot(b3[:,0],b3[:,1],color='brown')
plt.title('Espacio de fase caso 4')
plt.xlabel('Posición (m)')
plt.ylabel("Velocidad(m/s)")


plt.subplot(3,2,5)
plt.plot(b4[:,0],b4[:,1],color='darkblue')
plt.title('Espacio de fase caso 5')
plt.xlabel('Posición(m)')
plt.ylabel("Velociad(m/s)")


plt.subplot(3,2,6)
plt.plot(b[:,0],b[:,1],color='green')
plt.plot(b1[:,0],b1[:,1],color='red')
plt.plot(b2[:,0],b2[:,1],color='purple')
plt.plot(b3[:,0],b3[:,1],color='brown')
plt.plot(b4[:,0],b4[:,1],color='darkblue')
plt.title(' Espacio de fase de todos los casos')
plt.xlabel('Posición(m)')
plt.ylabel('Velocidad(m/s)')

plt.savefig('Diagfaseoscilador.jpg')
plt.show()


# In[8]:


r=OsciladorAmortiguado(y0,t,1.6,0.0123)
r1=OsciladorAmortiguado(y1,t,1.4,0.0134)
r2=OsciladorAmortiguado(y2,t,1.7,0.0145)
r3=OsciladorAmortiguado(y3,t,2.1,0.0156)
r4=OsciladorAmortiguado(y4,t,2.4,0.0167)

z=r.sol()
z1=r1.sol()
z2=r2.sol()
z3=r3.sol()
z4=r4.sol()

plt.figure(figsize=(20, 19))
plt.subplot(3,2,1)
plt.plot(t,z[:,0],label='y0',color='green')
plt.title('Solución subamortiguada caso 1')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,2)
plt.plot(t,z1[:,0],label='y1',color='red')
plt.title('Solución subamortiguada caso 2')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,3)
plt.plot(t,z2[:,0],label='y2',color='purple')
plt.title('Solución subamortiguada caso 3')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,4)
plt.plot(t,z3[:,0],label='y3',color='brown')
plt.title('Solución subamortiguada caso 4')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,5)
plt.plot(t,z4[:,0],label='y4',color='darkblue')
plt.title('Solución subamartiguada caso 5')
plt.xlabel('t(s)')
plt.ylabel("y(m)")
plt.legend()

plt.subplot(3,2,6)
plt.plot(t,z[:,0],label='y0',color='green')
plt.plot(t,z1[:,0],label='y1',color='red')
plt.plot(t,z2[:,0],label='y2',color='purple')
plt.plot(t,z3[:,0],label='y3',color='brown')
plt.plot(t,z4[:,0],label='y4',color='darkblue')
plt.title('Todos los casos amortiguados')
plt.xlabel('t(s)')
plt.ylabel('y(m)')
plt.legend()

plt.savefig('Osciladoramortiguado.jpg')
plt.show()


# In[9]:


plt.figure(figsize=(20, 19))
plt.subplot(3,2,1)
plt.plot(z[:,0],z[:,1],color='green')
plt.title('Espacio de fase caso 1')
plt.xlabel('Posición (m)')
plt.ylabel("Velocidad (m/s)")


plt.subplot(3,2,2)
plt.plot(z1[:,0],z1[:,1],color='red')
plt.title('Espacio de fase caso 2')
plt.xlabel('Posición (m)')
plt.ylabel("Velocidad (m/s)")


plt.subplot(3,2,3)
plt.plot(z2[:,0],z2[:,1],color='purple')
plt.title('Espacio de fase caso 3')
plt.xlabel('Posición (m)')
plt.ylabel('Velocidad (m/s)')


plt.subplot(3,2,4)
plt.plot(z3[:,0],z3[:,1],color='brown')
plt.title('Espacio de fase caso 4')
plt.xlabel('Posición (m)')
plt.ylabel("Velocidad (m/s)")


plt.subplot(3,2,5)
plt.plot(z4[:,0],z4[:,1],color='darkblue')
plt.title('Espacio de fase caso 5')
plt.xlabel('Posición (m)')
plt.ylabel("Velociad (m/s)")


plt.subplot(3,2,6)
plt.plot(z[:,0],z[:,1],color='green')
plt.plot(z1[:,0],z1[:,1],color='red')
plt.plot(z2[:,0],z2[:,1],color='purple')
plt.plot(z3[:,0],z3[:,1],color='brown')
plt.plot(z4[:,0],z4[:,1],color='darkblue')
plt.title(' Espacio de fase de todos los casos')
plt.xlabel('Posición (m)')
plt.ylabel('Velocidad (m/s)')

plt.savefig('Diagfaseosciladoramortiguado.jpg')
plt.show()


# In[ ]:




