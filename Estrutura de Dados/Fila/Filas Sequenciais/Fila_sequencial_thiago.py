class FilaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class FilaSequencial:
    def __init__(self):
        self.__dados=[] #inicia como uma lista vazia
    
    def __len__(self):
        return len(self.__dados)

    def vazia(self):
        return len(self)==0
    
    def tamanho(self):
        return len(self)
    
    def inicio(self):
        if self.vazia():
            raise FilaException(f'A fila está vazia!')
        return self.__dados[0]

    def inserir(self, dado):
        self.__dados.append(dado) #entra no final (Last In), o contrário seria .insert(0, dado) (First In)
    
    def remover(self):
        if self.vazia():
            raise FilaException(f'A fila está vazia')
        self.__dados.pop(0) #remove do inicio (Last Out), o contrário seria .pop() (First out)

    def __str__(self):
        return self.__dados.__str__()
    
    def imprimir(self):
        print(self.__str__())

if __name__=='__main__':
    try:
        nova_fila = FilaSequencial()

        for i in range(1,11):
            nova_fila.inserir(i*2)
        
        nova_fila.imprimir()

        for i in range(nova_fila.tamanho()):
            nova_fila.remover()
            nova_fila.imprimir()
        print(nova_fila.remover())
    except FilaException as fe:
        print(fe)