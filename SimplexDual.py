import numpy as np
from fractions import Fraction
from SeleccionarIndice import get_out_indice_dual,get_in_indice_dual

def simplex_dual(A,b,c,indices,fun=min,indices_no=[]):
    # inicializar variables
    mat=np.concatenate([A,b],axis=1) # Matriz del simplex
    c=np.array(c)
    z=-np.dot(c[indices],b)
    c-=np.dot(c[indices],A)
    
    costs=np.concatenate([c,z],axis=0) # Vector de costes

    while True:
        # Obtener el indice de entrada
        out_indice=get_out_indice_dual(mat[:,-1],fun)

        if None==out_indice: # Si no existe, la solucion es optima
            result=[Fraction(0) for i in range(len(A[0]))]
            for i in range(len(indices)):
                if indices[i]<len(A[0]):
                    result[indices[i]]=mat[i,-1]
            return mat[:,:len(mat[0])-1],mat[:,[len(mat[0])-1]],result,indices

        # Obtener el indice de salida
        in_indice=get_in_indice_dual(mat[:,:-1],costs[:-1],fun,out_indice,indices_no) #############

        if None==in_indice: # Si no existe, solucion no acotada
            return ######## TODO ##########
        
        # Actualizar Fila de salida
        mat[out_indice]/=mat[out_indice,in_indice] 
        # Actualizar el resto de valores
        for i in range(len(mat)):
            if i==out_indice:continue
            mat[i]-=mat[i][in_indice]*mat[out_indice]

        # Actualizar los indices
        indices[out_indice]=in_indice

        # Actualizar los costes
        costs-=costs[in_indice]*mat[out_indice]