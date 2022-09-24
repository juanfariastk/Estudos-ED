

class FilaCircularExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class FilaSequencialCircular:
    def __init__(self, tamanho:int=10):
        self.__inicio = 0
        self.__final= -1
        self.__tamanho = tamanho
        self.__ocupados = 0  #quantidade de elementos ocupados na fila, lembrando que ela tem um tamanho definido e pode ter espaços vazios...
        self.__itens = [None for i in range(tamanho)] #delimitando o tamanho

    def __len__(self):
        return self.__ocupados #o tamanho é os ocupados por justamente os ocupados serem os espaços que possuem algo, lembrando que a fila pode ter espaços vazios...

    def esta_vazia(self):
        return len(self)==0
    
    def esta_cheia(self):
        return self.__ocupados == self.__tamanho #se o numero e ocupados for igual ao tamanho, significa que não tem mais espaços na fila
    
    def tamanho(self):
        return len(self)
    
    def elemento(self, posicao): 
        #metodo que busca um elemento em uma posição
        try:
            assert posicao>0 and posicao<=len(self)
            inicio_fila = self.__inicio
            for i in range(posicao-1): #percorrendo a fila de acordo com a posição recebida
                inicio_fila = (inicio_fila+1)%self.__tamanho
            return self.__itens[inicio_fila]
        except AssertionError:
            raise FilaCircularExcept(f'Posição inválida!')
    
    def busca(self, item):
        inicio_fila= self.__inicio
        contador=0
        for i in range(len(self)):
            contador+=1
            if self.__itens[inicio_fila]==item:
                return contador
            inicio = (inicio+1)%self.__tamanho

        raise FilaCircularExcept(f'O item {item} não está na fila')
    
    def enfileira(self, item):
        if self.esta_cheia():
            raise FilaCircularExcept(f'A fila está cheia!')
        self.__final = (self.__final+1)%self.__tamanho
        self.__itens[self.__final]= item
        self.__ocupados+=1
    
    def desenfileira(self):
        if self.esta_vazia():
            raise FilaCircularExcept(f'A fila está vazia!')
        conteudo = self.__itens[self.__inicio]
        self.__inicio = (self.__inicio+1)%self.__tamanho
        self.__ocupados-=1
        return conteudo
    
    def __str__(self):
        if self.esta_vazia():
            raise FilaCircularExcept(f'fila está vazia')
        dados=''
        inicio = self.__inicio
        for i in range(len(self)):
            dados+=f' {self.__itens[inicio]} ' +'=>'
            inicio = (inicio+1)%self.__tamanho
        return dados
    
    def esvaziar(self):
        while (not self.esta_vazia()):
            self.desenfileira()
        

if __name__=='__main__':

    try:
        fila_circular = FilaSequencialCircular()

        for i in range(1,6):
            fila_circular.enfileira(i)
        print(fila_circular)
        

    except FilaCircularExcept as fce:
        print(fce)
    