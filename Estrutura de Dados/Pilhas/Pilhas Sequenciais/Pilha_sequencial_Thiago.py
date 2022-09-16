#criando exceção
class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
#criando a classe de pilha

class Pilha:

    def __init__(self):
        self._itens = [] #definindo a estrutura que vai guardar os dados
        
    #metodos da pilha

    #metodo se está vazio
    def vazio(self):
        return len(self._itens) == 0 #retorna um true ou false
    
    #metodo de tamanho da pilha

    def tamanho_pilha(self):
        return len(self._itens)
    
    #metodo que retorna o que está no topo da lista
    def topo(self):
        if self.vazio():
            raise PilhaException('A pilha está vazia')
        
        return self._itens[0]

    #metodo que insere um dado no topo da pilha, caso seja inserir no final, usar um append
    def insere_item(self, item):
        self._itens.insert(0, item)
    
    #metodo que remove o elemento do topo
    def remove_item(self):
        if self.vazio():
            raise PilhaException('A pilha está vazia')

        return self._itens.pop(0)
    
    #metodo __str__
    def __str__(self) -> str:
        return self._itens.__str__()

    #melhorando o retorno anterior com uma função
    def imprime_pilha(self)->str:
        print(self.__str__())


#instanciando a pilha 

if __name__ =='__main__':
    pilha_sequencial = Pilha()

    try:
        pilha_sequencial.topo()
    except PilhaException as pe:
        print(pe)
        
    for i in range(1,6):
        pilha_sequencial.insere_item(i*5)

    pilha_sequencial.imprime_pilha()
    pilha_sequencial.remove_item()
    pilha_sequencial.remove_item()
    pilha_sequencial.imprime_pilha()
    
