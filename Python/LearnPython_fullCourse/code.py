from math import *

# curso de python - learn python full course for beginners [tutorial];

caracter_name = "Jon"
frase = "teste geral de strings"
caracter_age = "35"
numa = 42
nome = ""

print("the name of my caracter is " + caracter_name)
print("the age of my caracter is " + caracter_age)
print(len(frase))
print(frase)
print(frase[3])
print(frase.index("s"))
print(frase.replace("geral", "suave"))

#fim da parte de string - 38:26 tempo atual.  -- Inicio da parte de numbers.

print (10 % 3) # apresenta o restante da divisao de inteiros
print(str(numa)  + " My favorite number")
print(pow(4, 6))
print(max(3, 4, 67, 8))
print(round(3.7))
print(floor(3.4))
print(ceil(55.4))
print(sqrt(36))

# parte de Get input from user

nome_stg = input("Enter your name: ")
print("Hello my friend " + nome_stg + "!")

