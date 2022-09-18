
class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, dado):
        self._proximo = None
        self._dado = dado

class FilaEncadeada:
    def __init__(self):
        self.__topo = None
        self.__final = None
        self.__tamanho = 0
    
    def __len__(self):
        return self.__tamanho
    
    def fila_vazia(self):
        return len(self)==0
    
    def inserir(self, dado): #a inserção ocorreu da seguinte forma: caso seja o primeiro elemento da fila, o topo e o fim serão iguais.
        #Agora, quando já estiver com algo, a inserção vai correr no final da fila
        #Logo, o final precisa reconhecer que tem um novo endereço para apontar, isto é o novo nó
        #Após isso, ele agora se torna o novo nó.

        no = No(dado)

        if self.__final is None:
            self.__final = no 
        else:
            self.__final._proximo = no
            self.__final = no
        
        if self.__topo is None:
            self.__topo = no
        
        self.__tamanho+=1
    
    def remover(self):
        if self.fila_vazia():
            raise FilaException(f'filha está vazia')
        self.__topo = self.__topo._proximo
        self.__tamanho-=1
    
    def topo_fila(self):
        aponta = self.__topo
        cont = 0
        while(aponta):
            if cont == len(self)-1:
                return f'{self.__topo._dado}'
            aponta = aponta._proximo
            cont+=1
    def modifica_item(self, item, item_novo):
        aponta = self.__topo
  
        while(aponta):
            if aponta._dado == item:
                aponta._dado = item_novo
                return f'item alterado!'
            aponta = aponta._proximo
    
    def modifica_posicao(self, posicao, item):
        apont = self.__topo
        cont=0
        try:
            assert posicao>0 and posicao<=len(self)
            while(apont):

                if cont == posicao-1:
                    apont._dado= item
                apont = apont._proximo
                cont+=1
        except AssertionError:
            raise FilaException(f'A fila só possui {len(self)} posições')

        
    
    def __str__(self):
        dados =''
        aponta = self.__topo
        while(aponta):
            dados+=f'{aponta._dado}:objeto'+' => '
            aponta = aponta._proximo
        return dados

if __name__=='__main__':
    fila = FilaEncadeada()
    
    for i in range(5):
        fila.inserir(i)
    
    print(fila)
    print(fila.topo_fila())

    fila.modifica_posicao(5,10)
    print(fila)
            


        