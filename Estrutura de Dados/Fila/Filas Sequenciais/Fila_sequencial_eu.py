class FilaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class FilaNutella:
    def __init__(self):
        self.__itens = []
    
    def __len__(self):
        return len(self.__itens)

    def fila_vazia(self):
        return len(self)==0
    
    def fila_tamanho(self):
        return len(self)
    
    def fila_inserir(self, dado):
        #self.__itens.append(dado) #adicionando no final
        self.__itens.insert(0, dado) #adicionando no inicio
    def fila_remover(self):
        if self.fila_vazia():
            raise FilaExcept(f' A FILA ESTÁ VAZIAAAAAA!!!   ')
        #self.__itens.pop(0) #removendo no inicio
        self.__itens.pop() #removendo no final
    
    def fila_topo(self):
        if self.fila_vazia():
            raise FilaExcept(f'A FILA ESTÁ VAZIAAAAAA!!!   ')
        #return self.__itens[0] #retornando o topo
        return self.__itens[len(self)-1]
    
    def __str__(self):
        dados=''
        for i in self.__itens:
            dados +=f'{i} '
        return dados

if __name__=='__main__':
    try:
        fila_nova = FilaNutella()

        for i in range(11):
            fila_nova.fila_inserir(i+7)
        
        print(fila_nova)
        print(fila_nova.fila_topo())
        for i in range(12):
            fila_nova.fila_remover()
        
        print(fila_nova)

        print(fila_nova.fila_topo())
    except FilaExcept as fe:
        print(fe)