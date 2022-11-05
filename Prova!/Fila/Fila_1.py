class FilaExcept(Exception):
    def __init__(self, msg) :
        super().__init__(msg)

class Fila:
    def __init__(self, tamanho=10):
        self.__inicio = 0
        self.__final = -1
        self.__tamanho = tamanho
        self.__ocupados = 0
        self.__dados = [None for i in range(tamanho)]
    
    def __len__(self):
        self.__ocupados
    
    def fila_vazia(self):
        return self.__ocupados==0
    
    def fila_cheia(self):
        return self.__ocupados==self.__tamanho
    
    def fila_tamanho(self):
        return self.__ocupados
    
    def tamanho_total(self):
        return self.__tamanho
    
    def enfileirar(self, item):
        self.__final = (self.__final+1)%self.__tamanho
        self.__dados[self.__final]=item
        self.__ocupados+=1
    
    def desenfileirar(self):
        dado = self.__dados[self.__inicio]
        self.__inicio = (self.__inicio+1)%self.__tamanho
        self.__ocupados-=1
        return dado
    
    def elemento(self, pos):
        apontador= self.__inicio
        dado=''
        for i in range(pos-1):
            apontador = (apontador+1)%self.__tamanho
        dado = self.__dados[apontador]
        return dado
    
    def busca(self, elemento):
        apontador = self.__inicio
        cont=1
        for i in range(self.__ocupados):
            if self.__dados[apontador]==elemento:
                return cont
            cont+=1
            apontador = (apontador+1)%self.__tamanho
    
    def concatenar(self, fila1:object):
        aux=Fila()
        while(not self.fila_vazia()):
            aux.enfileirar(self.desenfileirar())
        while(not fila1.fila_vazia()):
            self.enfileirar(fila1.desenfileirar())
        while(not aux.fila_vazia()):
            self.enfileirar(aux.desenfileirar())

    @classmethod
    def concatenar_alternado(cls, fila1:object, fila2:object, fila3:object):
        tamanho_filas = fila2.fila_tamanho()+fila3.fila_tamanho()
        cont=0
        try:
            assert tamanho_filas<=fila1.tamanho_total()
            for i in range(tamanho_filas):
                if cont%2==0:
                    fila1.enfileirar(fila2.desenfileirar())
                else:
                    fila1.enfileirar(fila3.desenfileirar())
                cont+=1
        except AssertionError:
            raise FilaExcept(f'Crie uma fila de tamanho maior para poder concatenar!')
                
    
    def __str__(self):
        dados=''
        apontador = self.__inicio
        for i in range(self.__ocupados):
            dados+=str(self.__dados[apontador])+'=>'
            apontador = (apontador+1)%self.__tamanho 
        return dados

if __name__=='__main__':
    fila_nova = Fila()
    fila_nova2 = Fila()
    fila_nova3=Fila()

    for i in range(1,6):
        fila_nova.enfileirar(i)
        fila_nova2.enfileirar(i+2)
    print(fila_nova)
    #fila_nova.desenfileirar()
    print(fila_nova2)

    Fila.concatenar_alternado(fila_nova3, fila_nova2, fila_nova)
    print(fila_nova3)
        

        
