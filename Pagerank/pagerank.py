
import numpy as np

N=int(input("\n HOW MANY OF PAGES:"))
d=0.85 #dumping factor
eps=1.0e-8 #epsilon quardratic error for convergence
print("PLEASE ENTER THE ADJANCENCY MATRIX FOR THE NETWORK")
print("TYPE 1 IF THERE IS A LINK FROM A PAGE i TO j ELSE TYPE 0")
links =[]
for i in range(0,N):
    L=[]
    for j in range(0,N):
        L.append(int(input('Page'+str(i+1)+' to Page'+str(j+1)+': ')))
    links.append(L)

D=(1-d)/N
C=np.ones((N,1),dtype=int)
C=np.matrix(C)

outboundL=np.zeros((N,),dtype=int)
for i in range (0,N):
    for j in range (0,N):
        if links[i][j]==1:
            outboundL[i]=outboundL[i]+1

M=np.zeros((N,N))
for i in range (0,N):
    for j in range (0,N):
        if links[j][i]==1:
            M[i][j]=1/outboundL[j]

M=np.matrix(M)

rank=np.matrix(np.full((N,1),1/N))

while True:
    ranknext=d*np.dot(M,rank)+ D*C
    diff = np.subtract(ranknext,rank)
    if np.linalg.norm(diff) < eps:
        break
    rank=ranknext