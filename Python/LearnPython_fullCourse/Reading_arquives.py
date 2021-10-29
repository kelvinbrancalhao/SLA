open("Empregados.txt", "r")
# cada letra no segunda item significa um item diferente
# r = read
# w = write
# a = append
# r+ = read and write
arquivo_empregados = open("Empregados.txt", "r")
print(arquivo_empregados.readable()) #retorna se é possivel ler o documento.
print(arquivo_empregados.read())

print(arquivo_empregados.readline())
print(arquivo_empregados.readline())

print(arquivo_empregados.readlines()[1]) #posiciona na linha desajada para fazer a leitura

for employee in arquivo_empregados.readlines():
    print(employee)

arquivo_empregados.close()

employees_arquive = open("Empregados.txt", "a")
employees_arquive.write("\nTobias - Recursos Humanos") # o \n é chamado de escape caracter
employees_arquive.close()
