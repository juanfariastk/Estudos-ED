
class FilaCircularExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class fila_circular:
    def __init__(self, tamanho=10):
        self._dados=[None for i in range(tamanho)]
        self._tamanho = tamanho
        self._final = -1
        self._inicio = 0 
        self._ocupados = 0
    
    def __len__(self):
        return self._ocupados
    
    def esta_cheia(self):
        return len(self)==self._tamanho
    
    def esta_vazia(self):
        return len(self)==0
    
    def enfileirar(self, item):
        if self.esta_cheia():
            raise FilaCircularExcept(f'a fila está cheia!')
        self._final = (self._final+1)%self._tamanho
        self._dados[self._final]=item
        self._ocupados+=1
    
    def desenfileirar(self):
        if self.esta_vazia():
            raise FilaCircularExcept(f'a fila está vazia!')
        dado = self._dados[self._inicio]
        self._inicio = (self._inicio+1)%self._tamanho
    
    def buscar_item(self, item):
        inicio = self._inicio
        for i in range(len(self)):
            if item == self._dados[inicio]:
                return f'O item [{item}] foi encontrado na posição {inicio+1}'
            inicio = (inicio+1)%self._tamanho
        raise FilaCircularExcept(f'Elemento não existe na fila!')

    def buscar_posicao(self, posicao):
        try:
            assert posicao<=len(self)
            aponta = self._inicio
            for i in range(posicao-1):
                aponta = (aponta+1)%self._tamanho
            return f'O item da posição {posicao} é {self._dados[aponta]}'
        except AssertionError:
            raise FilaCircularExcept(f'Esta posição é inválida!')
    
    def __str__(self):
        dados = ''
        aponta = self._inicio
        for i in range(len(self)):
            dados+=f'{self._dados[aponta]} '
            aponta = (aponta+1)%self._tamanho
        return dados

if __name__=='__main__':
    fila_nova = fila_circular()
    print(fila_circular())

    for i in range(1,11):
        fila_nova.enfileirar(i)
    
    print(fila_nova)

    print(fila_nova.buscar_posicao(8))
    print(fila_nova.buscar_item(10))

        
        