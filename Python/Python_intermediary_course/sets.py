# Sets são um conjunto de dados que é unordered, mutable, but without duplicates -  ou seja, nao é possivel duplicar
# elementos dentro de um set - se aplica bem ao emprego de descobrir diferentes contextos dentro de um conjunto.

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)

myset.discard(4)

print(myset)

odds = {1, 3, 5, 7}
evens = {1, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

u = odds.union(evens) # uni dois sets
print(u)

i = odds.intersection(prime) #compara os itens que se repetem e logo em seguida os armazena na variável
print(i)
