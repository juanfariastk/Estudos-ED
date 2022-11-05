class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No_cabeca:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0 
        #Assim, deu pra ver que o nó cabeça, na verdade, é quem faz o controle da fila em si
        #Então da pra dizer que a fila na verdade é um enorme nó cabeça

class No:
    def __init__(self, dado):
        self._item = dado
        self._proximo = None

    def __str__(self):
        return f' {self._item} '

    #Esse será o nó que ira sendo adicionado ao nó cabeça, lembrando que o nó cabeça, na verdade, é um conglomerado de nós

class FilaEncadeada:
    def __init__(self):
        self.__cabeca = No_cabeca()
    
    def __len__(self):
        return  self.__cabeca.tamanho
    
    def fila_tamanho(self):
        return self.__cabeca.tamanho

    def fila_vazia(self):
        return self.__cabeca.tamanho==0
    
    def elemento(self, posicao):
        try:
            assert posicao>0 and posicao<=self.__cabeca.tamanho
            apontador = self.__cabeca.inicio
            cont=1
            while(cont!=posicao):
                apontador = apontador._proximo
                cont+=1
            return apontador._item
        except AssertionError:
            raise FilaException(f'Erro ao encontrar o item')
    
    def buscar(self, dado):
        apontador = self.__cabeca.inicio
        contador = 0 
        while(apontador):
            contador+=1
            if apontador._item ==dado:
                return contador
            apontador = apontador._proximo

        raise FilaException(f'Elemento não existe')


    def enfileira(self, dado):
        no_novo = No(dado)
        if self.fila_vazia():
            self.__cabeca.inicio = no_novo
            self.__cabeca.final = no_novo
        else:
            self.__cabeca.final._proximo = no_novo
            self.__cabeca.final = no_novo
        self.__cabeca.tamanho+=1

    def desenfileira(self):
        dado_removido = self.__cabeca.inicio._item 
        self.__cabeca.inicio = self.__cabeca.inicio._proximo
        self.__cabeca.tamanho-=1
        return dado_removido
    
    @classmethod
    def combina(cls, fila1, fila2, fila3):
        aux1 = FilaEncadeada()
        aux2 = FilaEncadeada()
        fila_fim = FilaEncadeada()
        tamanho = fila2.__cabeca.tamanho + fila3.__cabeca.tamanho

        apontador1 = fila2.__cabeca.inicio
        while(apontador1):
            aux1.enfileira(fila2.desenfileira())
            apontador1 = apontador1._proximo
        
        apontador2 = fila3.__cabeca.inicio
        while(apontador2):
            aux2.enfileira(fila3.desenfileira())
            apontador2 = apontador2._proximo

        contador = 0 
        for i in range(tamanho):
            if contador%2==0:
                fila_fim.enfileira(aux1.desenfileira())
            else:
                fila_fim.enfileira(aux2.desenfileira())
            contador+1
        fila1.__cabeca = fila_fim.__cabeca

    def __str__(self):
        dado = ''
        apontador= self.__cabeca.inicio
        while(apontador):
            dado+=f'{apontador._item} ' + '=>'  
            apontador = apontador._proximo
        return dado
    
    def esvaziar_fila(self):
        while(not self.fila_vazia()):
            self.desenfileira()

fila_encadeada = FilaEncadeada()
fila_encadeada2 = FilaEncadeada()
fila_encadeada3 = FilaEncadeada()
for i in range(1,5):
    fila_encadeada.enfileira(i+1)
    fila_encadeada2.enfileira(i)


print(fila_encadeada)
print(fila_encadeada2)
FilaEncadeada.combina(fila_encadeada3, fila_encadeada, fila_encadeada2)
#print(fila_encadeada.elemento(2))
#print(fila_encadeada.buscar(5))
#print(fila_encadeada.desenfileira())
#print(fila_encadeada)

    
    
    