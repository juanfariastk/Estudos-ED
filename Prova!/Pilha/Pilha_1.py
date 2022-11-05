
from operator import contains


class PilhaExcept(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class No:
    def __init__(self, dado):
        self.proximo = None
        self.dado = dado

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
    
    def __len__(self):
        return self.__tamanho
    
    def pilha_vazia(self):
        return self.__tamanho==0
    
    def empilhar(self, item):
        novo_no = No(item)
        novo_no.proximo=self.__topo
        self.__topo = novo_no
        self.__tamanho+=1
    
    def desempilha(self):
        dado = self.__topo.dado
        self.__topo = self.__topo.proximo
        self.__tamanho-=1
        return dado
    
    def elemento_topo(self):
        topo = self.__topo.dado
        return topo 
    
    def sub_topo(self):
        subtopo = self.__topo
        subtopo = subtopo.proximo
        return subtopo.dado
    
    def base_pilha(self):
        contador=0
        apontador = self.__topo
        while(contador!=self.__tamanho-1):
            apontador = apontador.proximo
            contador+=1
        return apontador.dado
    
    def elemento(self, posicao):
        apontador = self.__topo
        contador=0
        while(contador!=posicao-1):
            apontador = apontador.proximo
            contador+=1
        return apontador.dado
    
    def busca(self, dado):
        apontador = self.__topo
        contador=1
        while(apontador):
            if apontador.dado==dado:
                return contador
            contador+=1
            apontador = apontador.proximo
    
    def concatenar(self, pilha1:object):
        aux=Pilha()
        while(not pilha1.pilha_vazia()):
            aux.empilhar(pilha1.desempilha())
        while(not aux.pilha_vazia()):
            self.empilhar(aux.desempilha())
    
    def inverter(self):
        aux = Pilha()
        while(not self.pilha_vazia()):
            aux.empilhar(self.desempilha())
        self.__topo = aux.__topo
    
    @classmethod
    def concatenar_pilhas(cls, pilha1:object, pilha2:object, pilha3:object):
        aux=Pilha()
        while(not pilha2.pilha_vazia()):
            aux.empilhar(pilha2.desempilha())
        while(not pilha3.pilha_vazia()):
            aux.empilhar(pilha3.desempilha())
        while(not aux.pilha_vazia()):
            pilha1.empilhar(aux.desempilha())
    
    def __str__(self):
        dados=''
        apontador = self.__topo
        while(apontador):
            dados+=str(apontador.dado)+'=>'
            apontador= apontador.proximo
        return dados
    
    def esvaziar(self):
        while(not self.pilha_vazia()):
            self.desempilha()


if __name__=='__main__':
    nova_pilha = Pilha()
    nova_pilha2=Pilha()
    for i in range(1,10):
        nova_pilha.empilhar(i)
        nova_pilha2.empilhar(i+1)
    
    #print(nova_pilha.busca(9))
    #nova_pilha.concatenar(nova_pilha2)
    print(nova_pilha)

    nova_pilha3=Pilha()
    Pilha.concatenar_pilhas(nova_pilha3, nova_pilha2, nova_pilha)
    print(nova_pilha3)
    print(nova_pilha3.sub_topo())
    print(nova_pilha3)
    nova_pilha3.inverter()
    print(nova_pilha3)
            
        


        

    


