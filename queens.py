# itertools
# https://docs.python.org/3.5/library/itertools.html

#permutations
# https://docs.python.org/3.5/library/itertools.html?highlight=permutations#itertools.permutations
# Return successive r length permutations of elements in the iterable.

#lens ## https://docs.python.org/3/library/functions.html#len

#len(s) Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

#coordenadas

#[3, 0, 4, 7, 5, 2, 6, 1]#


# N = numero filas
# sol = numero de soluciones
# cols = columnas (0,1,2,3,4,5,6,7)
# combo[i]+i es la intercepción 
# combo[i]-i se mueve desde la parte superior izquierda hacia abajo a la derecha
# set se utiliza ya que si en el movimiento se generan dos números, uno se archiva y el otro se cancela
# si la reina cae en la misma diagonal se obtienen menos de n soluciones

#usamos permutations para obtener length

from itertools import permutations

N=8
sol=0
cols = range(N)
for combo in permutations(cols):                      
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1
        print('Solución '+str(sol)+': '+str(combo)+'\n')  
        print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in combo) + "\n\n\n\n")


