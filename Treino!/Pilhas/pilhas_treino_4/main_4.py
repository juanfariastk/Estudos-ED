from pilha_4 import *

nova_pilha = PilhaEncadeada()
print(nova_pilha)

nova_pilha.empilhar(1)
nova_pilha.empilhar(2)
nova_pilha.empilhar(3)
nova_pilha.empilhar(4)

print(nova_pilha)

#nova_pilha.esvaziar_pilha_met_raiz()

print(nova_pilha.buscar_elemento(4))
print(nova_pilha.buscar_posicao(1))

nova_pilha.modificar_item(2,12)
print(nova_pilha)

#print(nova_pilha.desempilha_elementos(4))
#nova_pilha.esvaziar_pilha_met_raiz()

print(nova_pilha.sub_topo())

nova_pilha.desempilha_elementos(2)
    
print(nova_pilha.sub_topo())
print(nova_pilha.base_pilha())

nova_pilha.modificar_item(1, 17)

print(nova_pilha.base_pilha())

print(nova_pilha)