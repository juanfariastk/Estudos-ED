
class FilaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class NoFila:
    def __init__(self, dado):
        self._dado = dado
        self._proximo = None

class FilaEncadeada:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
        self.__final = None
    
    def __len__(self):
        return self.__tamanho

    def esta_vazia(self):
        return len(self)==0
    
    def tamanho_fila(self):
        return len(self)
    
    def inserir(self, dado):
        no_novo = NoFila(dado)

        if self.__final is None:
            self.__final = no_novo
        else:
            self.__final._proximo = no_novo 
            self.__final = no_novo 
        
        if self.__topo is None:
            self.__topo = no_novo
        self.__tamanho+=1
    
    def remover(self):
        if self.esta_vazia():
            raise (f'Fila VAZIA')
        self.__topo = self.__topo._proximo
        self.__tamanho-=1
    
    def percorrer(self, posicao):
        aponta = self.__topo
        cont = 0
        while(cont!=posicao-1):
            aponta = aponta._proximo
            cont+=1
        aponta._dado = 'FUI PERCORRIDO!!!'
        

    def __str__(self):
        dados=''
        aponta= self.__topo
        while(aponta):
            dados+=str(aponta._dado) +'=>'
            aponta = aponta._proximo
        return dados

if __name__=='__main__':
    teste = FilaEncadeada()
    for i in range(5):
        teste.inserir(i+3)

    print(teste)
    print('oi')
    #teste.remover()
    teste.percorrer(1)
    print(teste)


    

        