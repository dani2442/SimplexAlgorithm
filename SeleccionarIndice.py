"""
    Implementar los algoritmos para obtener el indice de entrada y de salida

    Primal Normal
    Primal Lexicografico
    Primal Bland

    Dual Normal
"""

import numpy as np
from fractions import Fraction as Fr
# Seleccionar Minimo indistintivamente (Primal)
def get_in_indice_Primal(c,fun,indices_no=[]):
    min_max=0
    for i in range(len(c)):
        if i in indices_no: continue
        if fun==min and c[i]<c[min_max]: min_max=i
        elif fun==max and c[i]>c[min_max]: min_max=i
    if fun(c[min_max],0)==0: return None
    else: return min_max

def get_out_indice_Primal(A,in_indice,indices):
    min=9999999
    min_indice=-1
    for i in range(len(A)):
        if A[i,in_indice]>0:
            if A[i,-1]/A[i,in_indice]<min: 
                min=A[i,-1]/A[i,in_indice]
                min_indice=i
    if min_indice==-1: return None
    else: return min_indice

# Selecciona Minimo indistivamente (Dual)
def get_out_indice_dual(b,indices_no=[]):
    min_indice=0
    for i in range(len(b)):
        #if i in indices_no: continue
        if b[i]<b[min_indice]: min_indice=i
    if min(b[min_indice],0)==0: return None
    else: return min_indice

def get_in_indice_dual(A,c,fun,out_indice,indices_no=[]):
    min_max=-1; value=-100000
    for i in range(len(A[0])):
        if i in indices_no: continue
        if A[out_indice,i]<0:
            if fun==min and -c[i]/A[out_indice,i]<-value: min_max=i;value=c[i]/A[out_indice,i]
            elif fun==max and c[i]/A[out_indice,i]<value: min_max=i;value=c[i]/A[out_indice,i]
    if min_max==-1: return None
    else: return min_max

# Regla lexicografica
def get_in_indice_Lexicografica(c,fun,indices_no=[]):
    min_max=0
    for i in range(len(c)):
        if i in indices_no: continue
        if fun==min and c[i]<c[min_max]: min_max=i
        elif fun==max and c[i]>c[min_max]: min_max=i
    if fun(c[min_max],0)==0: return None
    else: return min_max

def get_out_indice_Lexicografica(A,in_indice,indices):
    min=None
    compare=np.concatenate((A[:,[-1]],A[:,indices]),axis=1)
    for i in range(len(A)):
        if A[i,in_indice]>0:
            if min==None: min=i
            elif compare[i]/A[i,in_indice]<compare[min]/A[i,indice]:min=i
    return min

# Regla Bland
def get_in_indice_Bland(c,fun,indices_no=[]):
    for i in range(len(c)):
        if i in indices_no: continue
        if fun==min and c[i]<0: return i
        elif fun==max and c[i]>0: return i
    return None

def get_out_indice_Bland(A,in_indice,indices):
    min=9999999
    min_indice=-1
    for i in range(len(A)):
        if A[i,in_indice]>0:
            if A[i,-1]/A[i,in_indice]<min: 
                min=A[i,-1]/A[i,in_indice]
                min_indice=i
    if min_indice==-1: return None
    else: return min_indice


get_in_indice=get_in_indice_Primal
get_out_indice=get_out_indice_Primal