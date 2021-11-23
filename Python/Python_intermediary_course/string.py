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
