
class PilhaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
    
class Nos:
    def __init__(self, item):
        self._dado= item
        self._proximo = None

class Pilha_Encadeada:
    def __init__(self):
        self.__tamanho = 0
        self._topo = None
    
    def pilha_vazia(self):
        return len(self)==0
    
    def tamanho_pilha(self):
        return self.__tamanho
    
    def empilhar(self,item):
        no_atual = Nos(item)
        no_atual._proximo = self._topo #definindo o próximo dentro do nó como sendo o topo atual da pilha
        self._topo = no_atual # o topo agora é o nó atual
        self.__tamanho+=1 #o tamaho agora é incrementado
    
    def desempilhar(self):
        self._topo = self._topo._proximo #seleciona o topo, logo após define que o topo atual é o próximo elemento, fazendo assim o antigo nó ser excluído
        self.__tamanho-=1
    
    def elemento_topo(self):
        if self.pilha_vazia():
            return 'a pilha não tem topo, pois está VAZIA!'
        return self._topo._dado 

    def buscar_dado(self, item):
        apontador = self._topo
        contador_pilha=0
        while (apontador):
            if item == apontador._dado:
                return f'o item {item} foi encontrado no nó {self.__tamanho-contador_pilha}'
            apontador = apontador._proximo
            contador_pilha+=1
        raise PilhaException(f' o item não foi encontrado')
    
    def modificar_dado(self, item_antigo, item_novo):
        return

    def __str__(self):
        if self.pilha_vazia():
            return 'pilha está vazia!'
        dados=''
        ap = self._topo
        while(ap):
            dados+=str(ap._dado)+' '
            ap= ap._proximo
        return dados



    def __len__(self):
        return self.__tamanho
  
if __name__=='__main__':
    pilha_teste = Pilha_Encadeada()
    print(pilha_teste.pilha_vazia())

    pilha_teste.empilhar(0)
    pilha_teste.empilhar(2)
    pilha_teste.empilhar(3)

    print(pilha_teste.pilha_vazia())
    print(pilha_teste.tamanho_pilha())

    print(pilha_teste)

    print(pilha_teste.buscar_dado(3))
    pilha_teste()
'''
    pilha_teste.desempilhar()
    pilha_teste.desempilhar()

    print(pilha_teste)
    print(pilha_teste.tamanho_pilha())
'''



    