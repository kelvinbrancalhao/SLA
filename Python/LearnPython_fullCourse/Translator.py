
def tradutorM(frase):
    traducao = ""

    for letter in frase:
        if letter in "aeiouAEIOU":
            traducao = traducao + "g"
        else:
            traducao = traducao + letter

    return traducao

print(tradutorM(input("Digite uma frase: ")))