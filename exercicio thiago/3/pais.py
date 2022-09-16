
from class_pais import Pais

p1 = Pais('brazil','brasilia', 4000, 'argentina')
p1.adiciona_fronteira('uruguai')
p1.adiciona_fronteira('algumlugar')
print(p1.adiciona_fronteira('uruguai'))
print(p1.adiciona_fronteira('uruguai'))
print(p1.fronteira)