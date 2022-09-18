class FilaEncadeadaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, dado):
        self._proximo = None
        self._dado = dado

class FilaEncadeada:
    def __init__(self) :
        self._topo = None
        self._final = None
        self.__tamanho = 0
    
    def __len__(self):
        return self.__tamanho
    
    def vazia(self):
        return len(self)==0
    
    def tamanho(self):
        return len(self)
    
    def topo_fila(self):
        return self._topo._dado
    
    def inserir(self, dado):
        novo_no = No(dado)
        if self.vazia():
            self._topo = novo_no
            self._final = novo_no
        else:
            self._final._proximo = novo_no
            self._final = novo_no
        self.__tamanho+=1

    def remover(self):
        if self.vazia():
            raise FilaEncadeadaExcept(f'Fila vazia')
        self._topo = self._topo._proximo
        
    
    def __str__(self) -> str:
        if self.vazia():
            raise FilaEncadeadaExcept(f'A fila está vazia!')
        
        dados=''
        aponta = self._topo
        while(aponta):
            dados+=f'{aponta._dado} ' + '-> '
            aponta= aponta._proximo
        return dados

if __name__=='__main__':
    try:
        fila = FilaEncadeada()
        fila.inserir(1)
        fila.inserir(2)
        fila.inserir(3)

        fila.remover()
        fila.remover()
        fila.remover()
        print(fila)
    

    except FilaEncadeadaExcept as fee:
        print(fee)