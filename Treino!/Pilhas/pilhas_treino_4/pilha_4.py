

class PilhaEncadeadaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, dado):
        self._proximo = None
        self._item = dado

class PilhaEncadeada:
    def __init__(self):
        self.__topo= None
        self.__tamanho = 0
    
    def __len__(self):
        return self.__tamanho
    
    def tamanho_pilha(self):
        return len(self)
    
    def pilha_vazia(self):
        return len(self)==0
    
    def empilhar(self, dado):
        no_novo = No(dado)
        no_novo._proximo = self.__topo
        self.__topo = no_novo
        self.__tamanho+=1
    
    def desempilha(self):
        item = self.__topo._item
        self.__topo = self.__topo._proximo
        self.__tamanho-=1
        return item
    
    def desempilha_elementos(self,elementos):
        try:
            assert elementos>0 and elementos<=self.__tamanho
            ind=0
            while (ind!=elementos):
                self.desempilha()
                ind+=1
        except AssertionError:
            raise PilhaEncadeadaException(f'A pilha possui {self.__tamanho} elemmentos, digite uma quantidade de remoções válidas!')

    def sub_topo(self):
        try:
            assert not self.pilha_vazia() and self.__tamanho>1
            aponta = self.__topo
            aponta = self.__topo._proximo
            return f'o subtopo da pilha é {aponta._item}'
        except AssertionError:
            raise PilhaEncadeadaException(f'esta pilha não tem subtopo!')

    def base_pilha(self):
        if self.pilha_vazia():
            raise PilhaEncadeadaException(f'A PILHA ESTÁ VAZIA!!!!!! DISGRAÇAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        aponta = self.__topo
        cont = len(self)
        while(cont!=1):
            aponta=aponta._proximo
            cont-=1
        return f'O elemento encontrado na base foi {aponta._item}'

    def buscar_elemento(self, elemento):
        aponta = self.__topo
        contador=0
        while(aponta):
            if aponta._item == elemento:
                return f'O item {elemento} foi encontrado na posição {self.__tamanho-contador}'
            aponta = aponta._proximo
            contador+=1

    def inverter_pilha(self):
        aux = PilhaEncadeada()
        while not self.pilha_vazia():
            aux.empilhar(self.desempilha())
        self.__topo = aux.__topo
        final = self.__topo
        return final

        
    def buscar_posicao(self, posicao):
        aponta = self.__topo
        cont=0
        while(self.__tamanho-posicao!=cont):
            aponta = aponta._proximo
            cont+=1
        return f'O elemento encontrado na posição {posicao} foi {aponta._item}'

    def concatena_pilha(self, pilha:object):
        aux = PilhaEncadeada()
        while(not pilha.pilha_vazia()):
            aux.empilhar(pilha.desempilha())
        while(not aux.pilha_vazia()):
            print('concatenando...')
            self.empilhar(aux.desempilha())
        
    @classmethod
    def concatenar_pilhas(cls, pilha1:object, pilha2:object):
        pilha_inicio = PilhaEncadeada()
        pilha_final = PilhaEncadeada()

        while not pilha1.pilha_vazia():
            pilha_inicio.empilhar(pilha1.desempilha())
        while not pilha_inicio.pilha_vazia():
            pilha_final.empilhar(pilha_inicio.desempilha())
        while not pilha2.pilha_vazia():
            pilha_inicio.empilhar(pilha2.desempilha())
        while not pilha_inicio.pilha_vazia():
            pilha_final.empilhar(pilha_inicio.desempilha())

        return pilha_final
        
            
    def modificar_item(self, posicao, item):
        aponta = self.__topo
        cont = 0 
        while(aponta):
            if self.__tamanho-cont == posicao:
                aponta._item = item
            aponta = aponta._proximo
            cont+=1
    
    
    def __str__(self):
        dados_pilha=''
        aponta = self.__topo
        while(aponta):
            dados_pilha+=str(aponta._item)+' '
            aponta = aponta._proximo
        return dados_pilha
    
    def esvaziar_pilha_met_raiz(self):
        while not self.pilha_vazia():
            self.desempilha()
        

if __name__=='__main__':
    pass

