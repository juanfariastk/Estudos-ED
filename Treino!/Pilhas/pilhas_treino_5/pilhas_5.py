
class PilhaExcp(Exception):
    def __init__(self,args):
        super().__init__(args)

class No:
    def __init__(self, item) -> None:
        self._proximo = None
        self._dado = item

class Pilha:
    def __init__(self) -> None:
        self.__topo = None
        self.__tamanho = 0
    
    def __len__(self):
        return self.__tamanho
    
    def vazia(self):
        return len(self)==0
    
    def tamanho(self):
        return len(self)
    
    def empilhar(self, dado):
        no_novo = No(dado)
        no_novo._proximo = self.__topo
        self.__topo = no_novo
        self.__tamanho+=1
    
    def desempilhar(self):
        self.__topo = self.__topo._proximo
        self.__tamanho-=1
    
    def topo(self):
        return self.__topo._dado

    def subtopo(self):
        aponta = self.__topo
        aponta=aponta._proximo
        return f'O subtopo é o elemento {aponta._dado}'

    
    def busca(self, item):
        aponta = self.__topo
        while(aponta):
            if aponta._dado == item:
                return True
            aponta = aponta._proximo
    
    
    def buscar_posicao(self, posicao):
        aponta = self.__topo
        cont=0
        while(aponta):
            if cont==posicao-1:
                return f'{aponta._dado}'
            aponta= aponta._proximo
            cont+=1
    
    def modificar(self, item, novo_item):
        aponta = self.__topo
        while(aponta):
            if item == aponta._dado:
                aponta._dado = novo_item
                return True
            aponta = aponta._proximo
    
    def modificar_posicao(self, pos, novo_item):
        aponta = self.__topo
        cont = 0
        while(aponta):
            if cont == pos-1:
                aponta._dado = novo_item
            aponta = aponta._proximo
            cont+=1
    
    def __str__(self):
        dados =''
        aponta= self.__topo
        while(aponta):
            dados+=f'{aponta._dado}' +' => '
            aponta = aponta._proximo
        return dados
    
    def esvaziar(self):
        while not self.vazia():
            self.desempilhar()

if __name__=='__main__':
    pilha = Pilha()

    for i in range(10):
        pilha.empilhar(i)
    
    print(pilha)

    #pilha.desempilhar()
    #pilha.esvaziar()
    print(pilha.modificar_posicao(1,11))
    print(pilha)
    print('tamanho pilha: ',pilha.tamanho())
    print(pilha.topo())
    print(pilha.subtopo())
        

            

