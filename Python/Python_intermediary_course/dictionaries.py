myDict = {"name": "Max", "age": 28, "city": "New york"}
myDict2 = dict(name="Aurelion", age=27, city="Boston")

print(myDict)
print(myDict2)

# os dicionarios podem ser criados a partir de uma declaração específica ou pode ser a partir de uma função

value_name = myDict["name"]
print(value_name)

myDict["email"] = "max@gmail.com"
print(myDict)

del myDict["name"]
print(myDict)

myDict["name"] = "Max"
print(myDict)

myDict.pop("age")
print(myDict)

mydict_cpy = myDict.copy() # se voce nao usar a função copy o resultado vai ser que os mesmos identificadores vão apontar pro mesmo
                            #lugar na memória e alterando a copia você vai estar alterando o arquivo principal

mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(myDict)
