#primeiro ponto a destacar meu nobre
# a pilha(stack), neste caso se for encadeada, ela só vai ter o elemento do topo e o seu tamanho
# por ser encadeada, ela tem nós(node), nele teremos o conteúdo(data) e o proximo nó(next/ponteiro que aponta para o próximo)

#o next do ultimo elemento de uma lista encadeada é o None


#criando inicialmente a classe dos nós
import random

class No: #node
    def __init__(self, item):
        self.conteudo = item
        self.__proximo = None

class Pilha_encadeada: #criando a pilha
    def __init__(self):
        self.__tamanho = 0
        self.__topo = None
    
    def esta_vazia(self):
        return len(self)==0

    def empilhar(self, item):
        no_pilha= No(item) #adicionando o item dentro do nó
        no_pilha.__proximo = self.__topo #definindo pra onde o nó vai apontar, lembrando que o ultimo elemento vai apontar pro None
        self.__topo = no_pilha #definindo o topo como o ultimo nó criado
        self.__tamanho+=1 #aumentando o tamanho, já que um nó foi adicionado

    def desempilhar(self):
        if self.esta_vazia():
            return 'a pilha já está vazia!'
        no_pilha = self.__topo #selecionando o topo, isto é o ultimo elemento adicionado
        self.__topo = self.__topo.__proximo #definindo agora que o topo atual é o próximo nó, ou seja, o topo anterior não existe e o topo atual é o endereço que antes era o próximo, porém agora é o topo(é meio confuso mas uma hora vai!)
        self.__tamanho-=1 #retirando o tamanho do nó, já que um nó foi retirado
        return no_pilha.conteudo
    
    def pilha_topo(self):
        if self.esta_vazia():
            return 'a pilha está vazia!'
        return self.__topo.conteudo # lembre-se Juan, o topo na verdade é um objeto também! Se lembre que ele recebe o nó criado, sendo este um objeto!

    def __len__(self):
        return self.__tamanho
    
    def __str__(self):
        if self.esta_vazia():
            return f'pilha vazia!'
        dados = ''
        apontador = self.__topo
        while(apontador): #lembre-se Juan, uma horá o topo será None. None = False, em python.
            dados+=str(apontador.conteudo)+' '  #loop percorre o conteudo do nó que o apontador faz referência
            apontador = apontador.__proximo  #o loop agora faz o apontador ir para o próximo conteúdo    
        return dados

if __name__=='__main__':
    pilha_e = Pilha_encadeada()
    pilha_e.empilha(random.randint(2,8))
    pilha_e.empilha(random.randint(2,8))
    pilha_e.empilha(random.randint(2,8))
    print(pilha_e)
    pilha_e.desempilha()
    print(pilha_e)

