# primeira aula sobre listas e tupes
mylist = tuple(["Max", 28, "Boston"])
print(mylist)

item = mylist[1] #se colocar a index no negativo ele pega do fim para o começo
print(item)

if "Max" in mylist:
    print("Yes")
else:
    print("No")

my_list = list(mylist)
my_list = tuple(my_list)
# é possível trabalhar com conversar de itens quando trabalhamos com lista e tuples

a = (0, 1, 2, 3, 4, 5, 6, 7)

