friends = ["Kevin", "Karen", "Jim","Colan","José"]
lucky_numbers = [12, 14, 78, 65, 54]
print(friends[1])
print(friends[-1]) #com numeros negativos eu começo pegando sempre do fim da fila
print(friends[2:4])

friends[1] = "Maria"
print(friends[1])

friends.append("Marcelo")# adiciona um novo elemento a lista no final
#friends.extend(lucky_numbers) # Adiciona toda uma lista a fim da primeira
print(friends)

friends.insert(2, "Mario") #Insere um Novo elemento a lista na posiçao desejada sem deletar nenhum item
print(friends)

friends.remove("Jim") #remove um item atrelado a index

friends.pop(2) #remove um item da lista /  quando vazio retira o ultimo item
print(friends.index("Marcelo")) # da a posição do elemente selecionado = 4
friends.insert(1, "Jim")
friends.insert(4, "Jim")
print(friends)
print(friends.count("Jim")) #conta quantas vezes um mesmo valor aparece na lista.
friends.sort()  # Coloca em ordem alfabética de acordo com a ordem
# print(friends)
lucky_numbers.sort()
print(lucky_numbers)

print(friends) # esta linnha imprime uma lista específica.


