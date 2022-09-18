
class FilaNutellaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class FilaNutella:
    def __init__(self):
        self.__dados= []
    
    def __len__(self) -> int:
        return len(self.__dados)
    
    def esta_vazia(self) ->bool:
        return len(self)==0
    
    def tamanho(self) -> int:
        return len(self)
    
    def inserir_dado(self, item):
        self.__dados.append(item) #inserindo no final
    
    def remover_dado(self):
        self.__dados.pop(0) #removendo no inicio
    
    def topo(self):
        return self.__dados[0]
    
    def busca(self, item):
        try:
            assert not self.esta_vazia()
            for i in range(len(self)):
                if self.__dados[i] == item:
                    return f'O item {item} está na posição {i+1}'
                else:
                    return f'Este elemento não existe na fila!'
        except AssertionError:
            raise FilaNutellaExcept(f'A Fila está vazia!')

    
    def buscar_posicao(self, posicao):
        try:
            assert not self.esta_vazia()
            return f'O item da posição {posicao} é {self.__dados[posicao-1]}'
        except AssertionError:
            raise FilaNutellaExcept(f'A fila está vazia!')
        except IndexError:
            raise FilaNutellaExcept(f'A fila não tem esta posição!')
    
    def modifica(self, item, novo_item):
        try:
            assert not self.esta_vazia()
            for i in range(len(self)):
                if self.__dados[i]==item:
                    self.__dados[i]=novo_item
                    return f'Item modificado com sucesso!'
                else:
                    return f'Este item não existe na fila!'
        except AssertionError:
            raise FilaNutellaExcept(f'A fila está vaziaaa!!!')
                

    def modifica_posicao(self, posicao, novo_item):
        try:
            assert not self.esta_vazia()
            self.__dados[posicao-1]=novo_item
            return f'item modificado!'
        except AssertionError:
            raise FilaNutellaExcept(f'A fila está vazia DISGRAÇAAAAAAAAAAA!')
        except IndexError:
            raise FilaNutellaExcept(f'Esta posição não existe na fila!')

    def __str__(self):
        dados=''
        for i in self.__dados:
            dados+=f'{i} '
        return dados
    
    def esvaziar_fila(self):
        #self.__dados.clear()  ou vamos de outro método???!!!
        self.__dados=[]

            
            

if __name__=='__main__':
    fila = FilaNutella()

    print(fila)
     
    for i in range(5):
        fila.inserir_dado(i*4)
        print(fila)

    print(fila.topo())

    fila.remover_dado()

    print(fila.topo())

    print(fila)
    print(fila.buscar_posicao(4))

    print(fila.modifica(4,100))
    print(fila)
    print(fila.topo())

    print(fila.modifica_posicao(2,10))
    print(fila)

    fila.esvaziar_fila()

    print(fila)

    


