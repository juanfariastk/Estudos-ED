from pilha_3 import *

pilha = Pilha()

pilha.empilhar(5)
pilha.empilhar(6)
pilha.empilhar(7)
pilha.empilhar(8)
pilha.empilhar(9)
pilha.empilhar(10)

print(pilha)

print(pilha.modificar_posicao(6, 11))
pilha.modificar_posicao(2,5)
pilha.modificar_posicao(3,5)

print(pilha)
pilha.modificar_iguais(5,10)

print(pilha)
print(pilha.buscar(11))


