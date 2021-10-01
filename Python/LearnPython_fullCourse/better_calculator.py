
def calculadora(n1,ope,n2):
    if ope == "/":
        return n1/n2
    elif ope == "*":
        return n1*n2
    elif ope == "+":
        return n1+n2
    elif ope == "-":
        return n1-n2
    else:
        return ("Operador Inválido")


num1 = float(input("Entre o Primeiro Numero: "))
op = input("Digite o Operador: ")
num2 = float(input("Entre o Segundo Numero: "))

if op == "/" or op == "*" or op == "+" or op == "-":
     print(calculadora(num1, op, num2))
else:
    print("Operador Inválido")


