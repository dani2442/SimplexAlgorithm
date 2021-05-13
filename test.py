from Problema import Problema

# Simplex 
A=[[2,3,1],[4,1,2],[3,4,2]]
b=[5,11,8]
c=[-5,-4,-3]
signos=[-1,-1,-1]
fun=min

A=[[2,1,1],[1,2,3],[2,2,1]]
b=[2,5,6]
c=[3,1,3]
signos=[-1,-1,-1]
fun=max

# Metodo Dos Fases
A=[[1,1,1,0,0],[-1,1,0,-1,0],[1,-2,0,0,1]]
b=[5,1,6]
c=[2,1,-1,0,0]
signos=[0,0,0]
fun=min

A=[[1,1,1],[1,-1,2],[0,2,-1]]
b=[4,1,3]
c=[1,2,-4]
signos=[0,0,0]
fun=min

A=[[1,1,1,0],[1,-1,2,-1],[0,2,-3,1]]
b=[4,1,3]
c=[0,1,-1,1]
signos=[0,0,0]
fun=max

# Hoja 5
A=[[6,3,5],[3,4,5]]
b=[45,30]
c=[3,1,5]
signos=[-1,-1]
fun=max

A=[[1,4,3],[1,2,-1]]
b=[12,4]
c=[1,-3,-1]
signos=[0,0]
fun=min

A=[[-2,-1,-1,-1,1,0,0],[4,-2,5,1,0,1,0],[-4,1,-3,-1,0,0,1]]
b=[-9,8,-5]
c=[34,5,19,9,0,0,0]
signos=[0,0,0]
fun=min

P = Problema(A,b,c,signos,fun)
#P.Solve_Primal()
P.Solve_Dual()
print(P.Get_Solucion())
#print(P)
#print(P.Is_Optimizado())
#print(P.Get_Solucion())
print(P.Get_Coste_Funcion())
#print(P.Get_Problema_Dual())

#P.Set_Costes([2,1,5,0,0])
#P.Set_Terminos_Independientes([45,45])
#P.Set_Costes([-1,1,2,0,0])

#P.Set_Terminos_Independientes([13,8])

#P.Add_Variable([1,1],-2)

#P.Add_Restriccion([-3,-5,3,0,0],-10,-1)

print(P.Is_Optimizado())
#P.Solve_Primal()
P.Solve_Dual()
print(P.Get_Solucion())
print(P.Get_Coste_Funcion())

A=[[2,3,1],[4,1,2],[3,4,2]]
b=[5,11,8]
c=[-5,-4,-3]
signos=[-1,-1,-1]
fun=min

P = Problema(A,b,c,signos,fun)
P.Solve_Primal()
print(P)