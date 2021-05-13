from SimplexDual import simplex_dual
import numpy as np
from fractions import Fraction
from MetodoDosFases import MetodoDosFases
from SimplexPrimal import SimplexPrimal
Fraction.__repr__=Fraction.__str__

class Problema(object):
    def __init__(self,A,b,c,signos,fun=min,indices_base=[],indices_variables=[]):
        self.A = np.vectorize(Fraction)(A)
        self.b = np.vectorize(Fraction)([b]).T
        self.c = np.vectorize(Fraction)(c)
        self.signos = signos
        self.fun = fun
        self.indices_base = indices_base
        self.indices_variables = indices_variables
        self.indices_no_usa = []
        self.solucion = None
    
    def __str__(self):
        cad="\t|"
        for i in range(len(self.A[0])):
            cad+="x_"+str(i)+"\t"
        cad+="\n"
 
        for i in range(len(self.A)):
            if self.indices_variables!=[]:
                cad+="x_"+str(self.indices_variables[i])
            cad+="\t|"
            for j in range(len(self.A[0])):
                cad+=str(self.A[i,j])+"\t"
            cad+=str(self.b[i])
            cad+="\n"
        cad+="\t|"
        cost=self.c if self.indices_variables==[] else self.Get_Coste_Reducido()
        for i in range(len(self.A[0])):
            cad+=str(cost[i])+"\t"
        cad+="z-"+str(0 if self.indices_variables==[] else self.Get_Coste_Funcion())+"\t"
        cad+="\n"
        return cad

    def Print(self): return str(self)
    
    def Solve_Primal(self):
        if self.indices_base==[]:
            self.A,self.b,self.indices_base,self.indices_variables,self.indices_no_usa,coste=MetodoDosFases(self.A,self.b,self.c,self.signos,min)
            if coste!=0: return "Solución Infactibe"

        self.c=np.pad(self.c,(0,len(self.A[0])-len(self.c)),constant_values=Fraction(0))
        self.A,self.b,self.solucion,self.indices_variables,coste=SimplexPrimal(self.A,self.b,self.c,self.indices_variables,self.fun,self.indices_no_usa)

    def Solve_Dual(self):
        if self.indices_base==[]:
            indices=[i for i in range(len(self.A[0])-len(self.A),len(self.A[0]))]
            self.A,self.b,self.solucion,self.indices_variables=simplex_dual(self.A,self.b,self.c,indices,self.fun)
        else:
            self.A,self.b,self.solucion,self.indices_variables=simplex_dual(self.A,self.b,self.c,self.indices_variables,self.fun,self.indices_no_usa)

    def Get_Problema_Dual(self):
        A=self.A.T.copy()
        b=self.b.T[0].copy()
        c=self.c.copy()
        if self.fun==min: 
            fun=max
        else:
            c=-c
        for i in range(len(self.signos)):
            if self.signos[i]==-1:
                A[i]=-A[i]
                b[i]=-b[i]
            elif self.signos[i]==0:
                A=np.concatenate((A,-A[:,[i]]),axis=1)
                b=np.concatenate((b,-b[[i]]),axis=0)
                c=np.concatenate((c,c[[i]]),axis=0)
            else:
                pass        
        return Problema(A,c,b,fun)

    def Is_Optimizado(self):
        c=self.Get_Coste_Reducido()
        for i in range(len(c)):
            if i in self.indices_no_usa: continue
            if self.fun(0,c[i])!=0: return False
        for i in self.b:
            if i<0: return False
        return True

    def Get_Solucion(self):
        result=[Fraction(0) for i in range(len(self.A[0]))]
        for i in range(len(self.indices_variables)):
            result[self.indices_variables[i]]=self.b[i,0]
        return result

    def Get_Coste_Funcion(self):
        return np.dot(self.Get_Solucion(),self.c)

    def Get_Solucion_Dual(self):
        if self.Is_Optimizado():
            return "TODO"
        else: return "Necesita Optimizar"

    def Get_Coste_Reducido(self):
        return self.c-np.dot(self.c[self.indices_variables],self.A)

    def Add_Variable(self,a,c):
        a=np.vectorize(Fraction)([a]).T
        if self.indices_base!=[]:
            a=np.dot(self.A[:,self.indices_base],a)
        self.A=np.concatenate((self.A,a),axis=1)
        self.c=np.concatenate((self.c,[Fraction(c)]),axis=0)

    def Add_Restriccion(self,a,b,signo):
        a=np.vectorize(Fraction)(a)
        b=Fraction(b)
        if self.indices_variables!=[]:
            for i in range(len(self.indices_variables)):
                if self.A[i,self.indices_variables[i]]!=0:
                    print(self.b[i]*a[self.indices_variables[i]])
                    b-=self.b[i]*a[self.indices_variables[i]]
                    a-=self.A[i]*a[self.indices_variables[i]]
                    
        self.A=np.concatenate((self.A,np.array([a])),axis=0)
        self.b=np.concatenate((self.b,[b]),axis=0)
        self.signos+=[signo]

        self.indices_variables+=[len(self.A[0])]
        self.indices_base+=[len(self.A[0])]

        self.c=np.concatenate((self.c,[Fraction(0)]))
        a=[Fraction(0) for i in range(len(self.indices_base))]
        a[-1]=Fraction(1)
        self.A=np.concatenate((self.A,np.array([a]).T),axis=1)
    
    def Set_Costes(self,c):
        self.c= np.vectorize(Fraction)(c)

    def Set_Terminos_Independientes(self,b):
        self.b=np.dot(self.A[:,self.indices_base],np.vectorize(Fraction)([b]).T)