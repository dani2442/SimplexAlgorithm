import numpy as np
from fractions import Fraction
from SimplexPrimal import SimplexPrimal

# signos: {-1,0,1}->{leq,eq,geq}

def MetodoDosFases(A,b,c,signos,fun=min):
    w=[Fraction(0) for i in range(len(A[0]))]
    indices_base=[]
    inidices_base_1=[]
    for i in range(len(signos)):
        if b[i]<0: # Necesitamos tener valores positivos
            A[i]=-A[i]
            signos[i]=-signos[i]
            b[i]=-b[i]
        
        if signos[i]==-1:
            indices_base.append(len(A[0]))
            w.append(0)
            vec=np.array([[Fraction(0) for j in range(len(A))]])
            vec[0,i]=Fraction(1)
            A=np.concatenate((A,vec.T),axis=1)
        else:
            k=check_for_id(A, i)
            if k!=-1:
                indices_base.append(k)
                w[k]=0
                A[i]/=A[i,k]
                b[i]/=A[i,k]
            else:
                indices_base.append(len(A[0]))
                inidices_base_1.append(len(A[0]))
                w.append(1)
                vec=np.array([[Fraction(0) for j in range(len(A))]])
                vec[0,i]=Fraction(1)
                A=np.concatenate((A,vec.T),axis=1)

            if signos[i]==0:
                pass
            else:
                w.append(0)
                vec=np.array([[Fraction(0) for j in range(len(A))]])
                vec[0,i]=Fraction(-1)
                A=np.concatenate((A,vec.T),axis=1)
        
    indices_base_asociada=indices_base.copy()
    # Resolver la primera fase
    coste=0
    if len(inidices_base_1)!=0:
        A,b,w,indices_base,coste=SimplexPrimal(A,b,w,indices_base,fun)
        if coste!=0: return "Solucion Infactible"

    return A,b,indices_base_asociada,indices_base,inidices_base_1,coste
    
        
def check_for_id(A,i): 
    for k in range(len(A[0])):
        val=True
        for j in range(len(A)):
            if i!=j:
                if A[j,k]!=Fraction(0): val=False;break
            else:
                if A[j,k]<=0: val=False;break
        if val: return k
    return -1
        