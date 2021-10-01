print(2**4)

#criar uma função oara potencializar um número

def raise_to_exp(base,exp):
    result =1
    for index in range(exp):
        result = result * base

    return result

print (raise_to_exp(2,5))