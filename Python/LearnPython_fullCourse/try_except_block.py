try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError:
    print("Erro de Divisão por zero")
except ValueError:
    print("Entrada Inválida")