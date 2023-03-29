import numpy as np
import matplotlib.pyplot as plt
from mpmath import *

N=10000 #précision du calcul
x=[(1+i)/N for i in range (N)] #abscisses de 0 à 1

#probabilités
p_j=np.zeros(N,dtype=np.float64) #jeu
p_tb=np.zeros(N,dtype=np.float64) #tie-break
p_s=np.zeros(N,dtype=np.float64) #set AVEC tie-break
p_s2=np.zeros(N,dtype=np.float64) #set SANS tie-break
p_m=np.zeros(N,dtype=np.float64) #match

for i in range (N):
    p_j[i]=x[i]**4+4*x[i]**4*(1-x[i])+10*x[i]**4*(1-x[i])**2/(1-2*x[i]*(1-x[i]))
    p_tb[i]=x[i]**7+7*x[i]**7*(1-x[i])+28*x[i]**7*(1-x[i])**2+84*x[i]**7*(1-x[i])**3+210*x[i]**7*(1-x[i])**4+462*x[i]**7*(1-x[i])**5/(1-2*x[i]*(1-x[i]))
    p_s[i]=p_j[i]**6+6*p_j[i]**6*(1-p_j[i])+21*p_j[i]**6*(1-p_j[i])**2+56*p_j[i]**6*(1-p_j[i])**3+126*p_j[i]**6*(1-p_j[i])**4+252*p_j[i]**7*(1-p_j[i])**5+504*p_j[i]**6*(1-p_j[i])**6*p_tb[i]
    p_s2[i]=p_j[i]**6+6*p_j[i]**6*(1-p_j[i])+21*p_j[i]**6*(1-p_j[i])**2+56*p_j[i]**6*(1-p_j[i])**3+126*p_j[i]**6*(1-p_j[i])**4/(1-2*p_j[i]*(1-p_j[i]))
    p_m[i]=p_s[i]**3+3*p_s[i]**3*(1-p_s[i])+6*p_s[i]**2*(1-p_s[i])**2*p_s2[i]

#Affichage courbes
fig, ax = plt.subplots()
plt.plot(x,p_j,color='green',label='$p_{jeu}$')
plt.plot(x,p_s,color='blue',label='$p_{set}$ avec tie-break')
plt.plot(x,p_s2,color='cyan',label='$p_{set}$ sans tie-break')
plt.plot(x,p_m,color='red',label='$p_{match}$')
ax.set(xlim=(0,1.01), xlabel='$p$',ylabel='probabilités',ylim=(0,1.01))
plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.grid(True)
plt.legend()
plt.show()

#Tableau de valeurs
p=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

for i in range (0,11):
    p_j[i]=p[i]**4+4*p[i]**4*(1-p[i])+10*p[i]**4*(1-p[i])**2/(1-2*p[i]*(1-p[i]))
    p_tb[i]=p[i]**7+7*p[i]**7*(1-p[i])+28*p[i]**7*(1-p[i])**2+84*p[i]**7*(1-p[i])**3+210*p[i]**7*(1-p[i])**4+462*p[i]**7*(1-p[i])**5/(1-2*p[i]*(1-p[i]))
    p_s[i]=p_j[i]**6+6*p_j[i]**6*(1-p_j[i])+21*p_j[i]**6*(1-p_j[i])**2+56*p_j[i]**6*(1-p_j[i])**3+126*p_j[i]**6*(1-p_j[i])**4+252*p_j[i]**7*(1-p_j[i])**5+504*p_j[i]**6*(1-p_j[i])**6*p_tb[i]
    p_s2[i]=p_j[i]**6+6*p_j[i]**6*(1-p_j[i])+21*p_j[i]**6*(1-p_j[i])**2+56*p_j[i]**6*(1-p_j[i])**3+126*p_j[i]**6*(1-p_j[i])**4/(1-2*p_j[i]*(1-p_j[i]))
    p_m[i]=p_s[i]**3+3*p_s[i]**3*(1-p_s[i])+6*p_s[i]**2*(1-p_s[i])**2*p_s2[i]

    print("p=",p[i],"  |  p_set=",p_s[i],"  |  p_match=",p_m[i])