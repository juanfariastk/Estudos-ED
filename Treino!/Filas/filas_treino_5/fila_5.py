from ast import Assert
from xml.sax.handler import feature_external_ges


class FilaErro(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class FilaCircular:
    def __init__(self, tamanho=10):
        self.__inicio = 0
        self.__final = -1
        self.__tamanho = tamanho
        self.__ocupados = 0
        self.__dados = [None for i in range(tamanho)]
    
    def __len__(self):
        return self.__ocupados
    
    def fila_vazia(self):
        return self.__ocupados==0
    
    def fila_cheia(self):
        return self.__ocupados == self.__tamanho
    
    def enfileirar(self, dado):
        if self.fila_cheia():
            raise FilaErro(f'A fila está vazia')
        self.__final = (self.__final+1)%self.__tamanho
        self.__dados[self.__final] = dado
        self.__ocupados+=1
    
    def desenfileira(self):
        dado_atual = self.__dados[self.__inicio]
        self.__inicio = (self.__inicio+1)%self.__tamanho
        self.__ocupados-=1

        return dado_atual
    
    def elemento(self, dado):
        apontador = self.__inicio
        cont=0
        for i in range(len(self)):
            if self.__dados[apontador]==dado:
                return cont
            apontador = (apontador+1)%self.__tamanho
            cont+=1
    
    def busca(self, posicao):
        try:
            assert posicao>0 and posicao<=len(self)
            apontador = self.__inicio
            for i in range(posicao-1):
                apontador = (apontador+1)%self.__tamanho
            dado_encontrado = self.__dados[apontador]
            return dado_encontrado
        except AssertionError:
            raise FilaErro(f'Posição inválida!')
    
    @classmethod
    def combina(cls, fila_fim:object, fila_1:object, fila_2:object):
        contador = 0

        tamanho = len(fila_1)+len(fila_2)
        fila_nova = FilaCircular()
        fila_inicio = FilaCircular()
        fila_final = FilaCircular()

        for i in range(len(fila_1)):
            fila_inicio.enfileirar(fila_1.desenfileira())
        for i in range(len(fila_2)):
            fila_final.enfileirar(fila_2.desenfileira())

        for i in range(tamanho):
            if contador%2==0:
                fila_nova.enfileirar(fila_inicio.desenfileira())
            else: 
                fila_nova.enfileirar(fila_final.desenfileira())
            contador+=1
        for i in range(len(fila_nova)):
            fila_fim.enfileirar(fila_nova.desenfileira())

    def __str__(self):
        dados = ''
        apontador = self.__inicio
        for i in range(len(self)):
            dados+=str(self.__dados[apontador]) + ' => '
            apontador = (apontador+1)%self.__tamanho
        return dados



try:

    fila_nova = FilaCircular()
    fila_nova2 = FilaCircular()
    fila_nova3 = FilaCircular()
    for i in range(1,6):
        fila_nova.enfileirar(i-1)
        fila_nova2.enfileirar(i+1)
    
    print(fila_nova)
    print(fila_nova2)

    FilaCircular.combina(fila_nova3, fila_nova, fila_nova2)

    print(fila_nova3)
except FilaErro as fe:
    print(fe)


    
        
