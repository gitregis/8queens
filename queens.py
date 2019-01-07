# itertools
# https://docs.python.org/3.5/library/itertools.html

#permutations
# https://docs.python.org/3.5/library/itertools.html?highlight=permutations#itertools.permutations

#lens ## https://docs.python.org/3/library/functions.html#len

#len(s) Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

#For this problem we assume each represent the coordinate of each queen on a vector.
#The number on the element represents the row while the position on the vector represents the column.
#The coordinates for the picture above is given as:

#[3, 0, 4, 7, 5, 2, 6, 1]#

#We are eliminating Rook moves finding permutations of rows. This will ensure that the rows and columns do not overlap.
#Bishop moves are eliminated by using set() and number of queens, N. 
#We will check Bishop for both diagonals. If there is no overlap, the set of 8 diagonals will be unique and will have lenght 8.

from itertools import permutations

N=8
sol=0
cols = range(N)
for combo in permutations(cols):                      
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1
        print('Solución '+str(sol)+': '+str(combo)+'\n')  
        print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in combo) + "\n\n\n\n")
