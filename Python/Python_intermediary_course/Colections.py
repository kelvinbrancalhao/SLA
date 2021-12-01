# Collections implentam um tipo especial de container para alguns tipos de dados, e fornece alternativa com algumas
# alternativas se compararmos aos demais elementos.

# Collections: counter, namedtuple, OrderedDict, Defaultdict, deque.
from collections import namedtuple
from collections import Counter
from collections import OrderedDict # tem a capacidade de lembrar a ordem que os itens foram adicionados
from collections import deque # é possivel manipular os dados per qualquer um dos lados - esquerda ou direita
from collections import defaultdict # lista comum porem quando oitem nao existe ela exibe o valor padrao da DataType.
a = "aaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(list(my_counter.elements()))

Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)
