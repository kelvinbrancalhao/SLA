#itertools: product, permutations, combinations, accumulate, groupby, and finite iterators

from itertools import product # retorna todas as combinações possíveis de um imput em produto cartesiano
from itertools import permutations # retorna todas as ordens possíveis de um imput
from itertools import combinations, combinations_with_replacement # retorna todas as combinações possiveis de um determinado tamanho

#product -------------------------------------
a= [1,2]
b= [3,4]
prod = product(a,b) # produz um produto cartesiano.
print(list(prod))

#permutations --------------------------------
c= [1,2,3,4]
permt = permutations(c)
print(list(permt))

#combinations --------------------------------
d= [1,2,3,4]
comb = combinations(d, 3) # especificar o tamanho das combinações
print(list(comb)) # não repete os itens
f = [1,2,3,4]
comb_wr = combinations_with_replacement(d, 3)
print(list(comb_wr)) #repete os itens

