class FilaExcept(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class NoC:
    def __init__(self):
        self.inicio = None
        self.final  = None
        self.tamanho = 0 

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class FilaEncadeada:
    def __init__(self):
        self.__cabeca= NoC()

    def __len__(self):
        return self.__cabeca.tamanho
    
    def fila_vazia(self):
        return self.__cabeca.tamanho ==0
    
    def tamanho_fila(self):
        return self.__cabeca.tamanho
    
    def enfileirar(self, dado):
        no = No(dado)

        if self.fila_vazia():
            self.__cabeca.inicio = no
            self.__cabeca.final = no
        else:
            self.__cabeca.final.proximo = no
            self.__cabeca.final = no
        self.__cabeca.tamanho+=1
    
    def desenfileira(self):
        if self.fila_vazia():
            raise FilaExcept(f'A fila está vazia')
        dado_removido = self.__cabeca.inicio.dado
        self.__cabeca.inicio = self.__cabeca.inicio.proximo
        self.__cabeca.tamanho-=1
        return dado_removido

    def elemento(self, posicao):
        if self.fila_vazia():
            raise FilaExcept(f'A fila está vazia')
        try:
            assert posicao>0 and posicao<=self.__cabeca.tamanho
            apontador = self.__cabeca.inicio
            contador = 1
            while(contador!=posicao):
                apontador = apontador.proximo
                contador+=1
            return f'{apontador.dado}'
        except AssertionError:
            raise FilaExcept(f'Posição inexistente')
    
    def busca(self, elemento):
        if self.fila_vazia():
            raise FilaExcept(f'A fila está vazia!')
        apontador = self.__cabeca.inicio
        contador=0
        while(apontador):
            if apontador.dado == elemento:
                return contador
            apontador = apontador.proximo
            contador+=1
        raise FilaExcept(f'Elemento não pertence a esta fila!')
    
    def __str__(self):
        dados=''
        apontador = self.__cabeca.inicio
        while(apontador):
            dados+=f' {apontador.dado} => '
            apontador = apontador.proximo 
        return dados

fila = FilaEncadeada()

for i in range(1,7):
    fila.enfileirar(i)

print(fila)

fila.desenfileira()


print(fila)
print(fila.busca(3))
print(fila.elemento(2))
#print(fila)

