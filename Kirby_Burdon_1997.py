import matplotlib.pyplot as plt
import numpy as np
from decimal import *
from numpy import random as random
getcontext().prec=17
# Model defintion
# Fig 1
# def gfg(q,n,k,a,t,c,s,M): # Function takes additional parameter M for mutation rate
#     p=1-q
#     N=(n*(1-k+(1-q**2)*a))/(1-(1-q**2)*t+n*((1-q**2)*(a+t)-k))
#     P=(p*(1-c-s*(1-t)+N*s*(k-a-t)))/(1-s+N*k*s+(1-q**2)*(t*s-c-N*s*(a+t)))
#     # With Mutation M
#     N=(N+M*(1.-2.*N))
#     Q=1.0-P
#     #Q=(Q+M*(1-2*Q))
#     Q=Q+M*(1.-2.*Q)
#     return N,Q
# Fig 2
# def gfg(q,n,k,a,t,c,s,M): # Function takes additional parameter M for mutation rate
#     p=1-q
#     N=(n*(1-k+(1-q**2)*a))/(1-(1-q**2)*t+n*((1-q**2)*(a+t)-k))
#     P=(p*(1-c-s*(1-t)+n*s*(k-a-t)))/(1-s+n*k*s+(1-q**2)*(t*s-c-n*s*(a+t)))
#     # With Mutation M
#     N=(N+M*(1.-2.*N))
#     Q=1.0-P
#     #Q=(Q+M*(1-2*Q))
#     Q=Q+M*(1.-2.*Q)
#     return N,Q
# Fig3
# def gfg(q,n,k,a,t,c,s,M): # Function takes additional parameter M for mutation rate
#     p=1-q
#     N=(n*(1-k+(1-q**2)*a))/(1-(1-q**2)*t+n*((1-q**2)*(a+t)-k))
#     P=(p*(1-c-s*(1-t)+N*s*(k-a-t)))/(1-s+N*k*s+(1-q**2)*(t*s-c-N*s*(a+t)))
#     # With Mutation M
#     N=(N+M*(1-2*N))*(1+random.uniform((-0.5)/(1e4),0.5/(1e4)))#(1+random.uniform(0,1/(1e4)))#
#     Q=1.0-P
#     Q=(Q+M*(1-2*Q))*(1+random.uniform((-0.5)/(2.0*1e4),0.5/(2.0*1e4)))#(1+random.uniform(0,1/(1e4)))#
#     return round(N,4),round(Q,4)




# Fixed point function, just in case
# STILL IN TERMS OF P
def eqpoint(k,a,t,c,s):
    neq=(t*s-c)/(t*s+a*s)
    peq=1-np.sqrt(1-k/(a+t))
    return neq,peq
# Model parameters
K=0.3
A=0.0
T=1.0
C=0.03
S=0.8
tmax=[200,400,200]

QINITIAL=0.999 # Initializing q=0.999
NINITIAL=0.001
QTEMP=QINITIAL
NTEMP=NINITIAL
q_freq=[]
n_freq=[]
q_freq.append(QINITIAL) # This is r
n_freq.append(NINITIAL)
# Range of mutation rates
#M=[0.0,1e-10,1e-6,1e-4]


###############################################################################################################
# Fig 2 generator
# M=[0.0,1e-4,1e-4,1e-10]
# f,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
# AX=[ax1,ax2,ax3,ax4]
# NINIT=[0.9,0.001,0.9,0.001]
# QINIT=[0.9,0.999,0.9,0.999]
# i=0
# NumIter=3
# markerstyle=['k+-','kx-','k.-']
# tmax=500
# for m in M:
#     q_freq=[]
#     n_freq=[]
#     QINITIAL=QINIT[i]
#     NINITIAL=NINIT[i]
#     QTEMP=QINITIAL
#     NTEMP=NINITIAL
#     q_freq.append(QTEMP)
#     n_freq.append(NTEMP)
#     for time in range(0,tmax):
#         # In case you want to play with the precision
#         # NTEMP,PTEMP=gfg(Decimal(PTEMP),Decimal(NTEMP),Decimal(k),Decimal(A),Decimal(T),Decimal(c),Decimal(S))
#         NTEMP,QTEMP=gfg(QTEMP,NTEMP,K,A,T,C,S,m)
#         q_freq.append(QTEMP)
#         n_freq.append(NTEMP)
#     AX[i].plot(n_freq,q_freq,markerstyle[j],label='Mut Rate='+str(m))
#     AX[i].set_xlim([-0.1,1.1])
#     AX[i].set_ylim([-0.1,1.1])
#     AX[i].plot(NINITIAL,QINITIAL,'ko')
#     i=i+1

# plt.show()
###############################################################################################################



# ###############################################################################################################
# # Fig 3 generator
# M=[1e-4,1e-5,1e-6]
# f,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
# AX=[ax1,ax2,ax3]

# i=0
# NumIter=3
# markerstyle=['k+-','kx-','k.-']
# for m in M[0:3]:
#     for j in range(0,NumIter):
#         q_freq=[]
#         n_freq=[]
#         QTEMP=QINITIAL
#         NTEMP=NINITIAL
#         q_freq.append(QTEMP)
#         n_freq.append(NTEMP)
#         for time in range(0,tmax[i]):
#             # In case you want to play with the precision
#             # NTEMP,PTEMP=gfg(Decimal(PTEMP),Decimal(NTEMP),Decimal(k),Decimal(A),Decimal(T),Decimal(c),Decimal(S))
#             NTEMP,QTEMP=gfg(QTEMP,NTEMP,K,A,T,C,S,m)
#             q_freq.append(QTEMP)
#             n_freq.append(NTEMP)
#         AX[i].plot(n_freq,q_freq,markerstyle[j],label='Mut Rate='+str(m))
#         AX[i].set_xlim([-0.1,1.1])
#         AX[i].set_ylim([-0.1,1.1])
#         AX[i].plot(NINITIAL,QINITIAL,'ko')
#     i=i+1
# for i in range(0,3):
#     q_freq=[]
#     n_freq=[]
#     QINITIAL=0.83667
#     NINITIAL=0.9625
#     QTEMP=QINITIAL*(1+random.uniform((-0.5)/(2.0*1e4),0.5/(2.0*1e4)))
#     NTEMP=NINITIAL*(1+random.uniform((-0.5)/(1e4),0.5/(1e4)))
#     q_freq.append(round(QTEMP))
#     n_freq.append(round(NTEMP))
#     m=1e-5
#     tmax=5000
#     for time in range(0,tmax):
#         # In case you want to play with the precision
#         # NTEMP,PTEMP=gfg(Decimal(PTEMP),Decimal(NTEMP),Decimal(k),Decimal(A),Decimal(T),Decimal(c),Decimal(S))
#         NTEMP,QTEMP=gfg(QTEMP,NTEMP,K,A,T,C,S,m)
#         q_freq.append(QTEMP)
#         n_freq.append(NTEMP)
#     ax4.plot(n_freq[-100:-1],q_freq[-100:-1],markerstyle[i],label='Mut Rate='+str(m))
#     ax4.set_xlim([-0.1,1.1])
#     ax4.set_ylim([-0.1,1.1])
# #    ax4.plot(NINITIAL,QINITIAL,'bo')

# plt.show()
# ###############################################################################################################

