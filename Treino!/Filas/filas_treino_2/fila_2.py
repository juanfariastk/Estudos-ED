class FilaSequencialCircularExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Fila_sequencial_circular:
    def __init__(self, tamanho=10):
        self.__dados = [None for i in range(tamanho)]
        self.__inicio = 0  #removemos os itens pelo inicio
        self.__final = -1  #adicionamos os itens ao final 
        self.__ocupados =0  #quantidade de espaços já ocupados, logo também teremos a quantidade disponivel por meio dos ocupados
        self.__tamanho = tamanho
    
    def __len__(self):
        return self.__ocupados
    
    def fila_vazia(self):
        return len(self)==0
    
    def fila_cheia(self):
        return len(self)==self.__tamanho
    
    def enfileirar(self, dado):
        if self.fila_cheia():
            raise FilaSequencialCircularExcept(f'A fila está cheia')
        
        self.__final = (self.__final+1)%self.__tamanho #percorre o final da lista somando +1 a posição
        self.__dados[self.__final] = dado #adiciona o dado na posição criada
        self.__ocupados +=1  #incrementa os ocupados 
    
    def desenfileirar(self):
        if self.fila_vazia():
            raise FilaSequencialCircularExcept(f'a fila está cheia!!!')
        dado = self.__dados[self.__inicio] 
        self.__inicio = (self.__inicio+1)%self.__tamanho
        self.__ocupados-=1
        return dado
    
    def buscar_elemento(self, elemento):
        apontador = self.__inicio
        for i in range(len(self)):
            if elemento == self.__dados[apontador]:
                return f'o item {elemento} foi encontrado na posição {apontador+1}'
            apontador = (apontador+1)%self.__tamanho
        raise FilaSequencialCircularExcept(f'o elemento não está na fila')
    
    def buscar_posicao(self, posicao):
        try:
            assert posicao<=len(self)
            apontador = self.__inicio
            for i in range(posicao-1):
                apontador = (apontador+1)%self.__tamanho
            return self.__dados[apontador]
        except AssertionError:
            raise FilaSequencialCircularExcept(f'Posição Inválida')

    # O macete é, caso queira percorrer, usar o inicio. 
    # Para adicionar, usamos o final. Somente e apenas isso.

    def __str__(self):
        dados=''
        apontador = self.__inicio
        for i in range(len(self)):
            dados+=f'{self.__dados[apontador]}' + '=>'
            apontador = (apontador+1)%self.__tamanho
        return dados

if __name__ =='__main__':
    fila_circular = Fila_sequencial_circular()

    print(fila_circular.fila_cheia())
    print(fila_circular.fila_vazia())

    for i in range(1,11):
        fila_circular.enfileirar(i+1)
    
    print(fila_circular)

    print(fila_circular.desenfileirar())

    print(fila_circular)

    print(fila_circular.buscar_elemento(11))

    print(fila_circular.buscar_posicao(4))