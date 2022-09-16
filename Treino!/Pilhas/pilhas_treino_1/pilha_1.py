import random

class PilhaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Pilha:
    def __init__(self):
        self.__dados=[]
        self.__tamanho=5
    

    def esta_vazia(self):
        return len(self.__dados)==0
    
    def tamanho_pilha(self):
        return len(self.__dados)

    def empilhar(self, conteudo):
        try:
            assert len(self.__dados)<self.__tamanho
            self.__dados.append(conteudo)
        except AssertionError:
            raise PilhaException(f'Pilha está cheia!')

    def desempilha(self):
        try:
            return self.__dados.pop()
        except:
            raise PilhaException(f'a pilha já está vazia!')
    
    def pilha_topo(self):
        try:
            return self.__dados[len(self.__dados)-1]
        except:
            raise PilhaException(f'A pilha está vazia!')
    
    def modifica_elemento(self, posicao, elemento):
        try:
            self.__dados[posicao-1]=elemento
        except IndexError:
            raise PilhaException(f'A posição {posicao} é inválida, a pilha possui atualmente {self.tamanho_pilha()} elementos')
    
    def pesquisar_elemento(self, elemento):
        for i in range(len(self.__dados)):
            if self.__dados[i]==elemento:
                return f'Elemento {elemento} foi encontrado na posição {i+1}'
        raise PilhaException(f'Elemento {elemento} não encontrado ou inválido')
        
    
    def __str__(self):
        dados=''
        for i in self.__dados:
            dados+=f'{i}'
        return dados
    
    def esvaziar_tudo(self):
        self.__dados.clear()

if __name__=='__main__':
    try:
        pilha1 = Pilha()
        print('pilha está vazia?',pilha1.esta_vazia())

        pilha1.empilhar(random.randint(2,9))
        pilha1.empilhar(random.randint(2,9))
        pilha1.empilhar(random.randint(2,9))
        pilha1.empilhar(random.randint(2,9))
        pilha1.empilhar(random.randint(2,9))
        pilha1.empilhar(random.randint(2,9))
        print('pilha está vazia?', pilha1.esta_vazia())

        print(pilha1)

        print(pilha1.pesquisar_elemento(11))
        #pilha1.modifica_elemento(8,10)
        print(pilha1.pilha_topo())

    except PilhaException as p_e:
        print(p_e)



        