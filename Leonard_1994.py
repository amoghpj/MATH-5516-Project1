import matplotlib.pyplot as plt
import numpy as np
from decimal import *
getcontext().prec=17

def gfg(p,n,k,a,t,c,s):
    q=1-p
    N=(n*(1-k+(1-q**2)*a))/(1-(1-q**2)*t+n*((1-q**2)*(a+t)-k))
    P=(p*(1-c-s*(1-t)+N*s*(k-a-t)))/(1-s+N*k*s+(1-q**2)*(t*s-c-N*s*(a+t)))
    return N,P
def eqpoint(k,a,t,c,s):
    neq=(t*s-c)/(t*s+a*s)
    peq=1-np.sqrt(1-k/(a+t))
    return neq,peq
tmax=165
p_freq=list()
n_freq=list()
K=0.3
A=0.0
T=1.0
C=0.03
S=0.8
PTEMP=0
NTEMP=0
PINITIAL=0.163
NINITIAL=0.2

###################################
#INITIALIZATION
PTEMP=PINITIAL
NTEMP=NINITIAL
p_freq.append(PINITIAL)
n_freq.append(NINITIAL)

for time in range(0,tmax):
    #NTEMP,PTEMP=gfg(Decimal(PTEMP),Decimal(NTEMP),Decimal(K),Decimal(A),Decimal(T),Decimal(C),Decimal(S))
    NTEMP,PTEMP=gfg(PTEMP,NTEMP,K,A,T,C,S)
    
    p_freq.append(PTEMP)
    n_freq.append(NTEMP)
plt.plot(NINITIAL,PINITIAL,'k.')

NEQ,PEQ=eqpoint(K,A,T,C,S)
plt.plot(NEQ,PEQ,'ko')
plt.plot(n_freq,p_freq,'k')
plt.xlim([0,1])
plt.ylim([0,1])
plt.show()
