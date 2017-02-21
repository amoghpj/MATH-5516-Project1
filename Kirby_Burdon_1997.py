import matplotlib.pyplot as plt
import numpy as np
from decimal import *
getcontext().prec=17
# Model defintion
def gfg(q,n,k,a,t,c,s,M): # Function takes additional parameter M for mutation rate
    p=1-q
    N=(n*(1-k+(1-q**2)*a))/(1-(1-q**2)*t+n*((1-q**2)*(a+t)-k))
    P=(p*(1-c-s*(1-t)+N*s*(k-a-t)))/(1-s+N*k*s+(1-q**2)*(t*s-c-N*s*(a+t)))
    # With Mutation M
    N=N+M*(1-2*N)
    Q=1-P
    Q=Q+M*(1-2*Q)
    return N,Q
# Fixed point function, just in case
# STILL IN TERMS OF P
def eqpoint(k,a,t,c,s):
    neq=(t*s-c)/(t*s+a*s)
    peq=1-np.sqrt(1-k/(a+t))
    return neq,peq
# Model parameters
K=0.3
A=0.0
T=1
C=0.03
S=0.8
tmax=500

QINITIAL=0.999 # Initializing q=0.999
NINITIAL=0.001
QTEMP=QINITIAL
NTEMP=NINITIAL
q_freq=[]
n_freq=[]
q_freq.append(QINITIAL) # This is r
n_freq.append(NINITIAL)
# Range of mutation rates
M=[0,1e-10,1e-6,1e-4]
f,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
AX=[ax1,ax2,ax3,ax4]

i=0

for m in M:
    q_freq=[]
    n_freq=[]
    QTEMP=QINITIAL
    NTEMP=NINITIAL
    q_freq.append(QTEMP)
    n_freq.append(NTEMP)
    for time in range(0,tmax):
        # In case you want to play with the precision
        # NTEMP,PTEMP=gfg(Decimal(PTEMP),Decimal(NTEMP),Decimal(k),Decimal(A),Decimal(T),Decimal(c),Decimal(S))
        NTEMP,QTEMP=gfg(QTEMP,NTEMP,K,A,T,C,S,m)
        q_freq.append(QTEMP)
        n_freq.append(NTEMP)
    AX[i].plot(n_freq,q_freq,'k',label='Mut Rate='+str(m))
    AX[i].set_xlim([-0.1,1.1])
    AX[i].set_ylim([-0.1,1.1])
    AX[i].plot(NINITIAL,QINITIAL,'bo')
    i=i+1
plt.show()
