# criar Matrizes / listas bidimencioanis

# um nested forloop é um sistema de loop dentro do loop


numbers_2d = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,18,19,20]
]
# O primeiro número é sempre a linha e somente depois vem a coluna.

print(numbers_2d[2][3])

for row in numbers_2d:
    print(row)

for row in numbers_2d:
    for col in row:
        print(col)



