mystring = 'I\'am a programer'
thestring = "Hello Word"
stringi = "Esse é uma tentativa interessante"

print(mystring)

string2 = """"I'm a programer """

substring1 = mystring[1:5]
print(substring1)

print(thestring.startswith("Hello"))
print(thestring.endswith("rd"))
print(thestring.find("o"))
print(thestring.count("o"))
print(thestring.replace("universe", "World"))

# Strings em python possuem diversas funções agregadas para constituir um mesmo tipo de função

My_list = thestring.split()
print(My_list)

newList = stringi.split(" ")
print(newList)

newString = ''.join(newList)
print(newString)

var = 3
my_string = "The variable is %d" % var # é possivel concatenar dentro da strinf com o simbolo % + a letra do tipo da
                                        # variável que está sendo concatenada.
print(my_string)

var2 = 2.5984
my_string2 = "The variable is {:.2f}".format(var2) #formata e faz o aredondamento.
print(my_string2)


