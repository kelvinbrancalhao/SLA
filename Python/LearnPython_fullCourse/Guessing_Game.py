#a idéia é limitar o numero de vezes que o usuario pode adivinhar a palavra

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
    guess = input("Diga a palavra secreta: ")
    guess_count +=1


if guess == secret_word:
    print("Parabéns você acertou")
else:
    print("Você ficou sem tentativas, talvez na próxima")

